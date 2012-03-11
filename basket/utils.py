from basket.models import Basket
from music.models import Music
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.conf import settings
import decimal
import random
import os
import zipfile

CART_ID_SESSION_KEY = 'cart_id'

#GET THE CURRENT USERS CART ID, SETS NEW ONE IF BLANK
def _basket_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_basket_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_basket_id():
    basket_id = ''
    characters = "ABCDEFGHIJKLMNPORSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"
    basket_id_length = 50
    for y in range(basket_id_length):
        basket_id += characters[random.randint(0, len(characters)-1)]
    return basket_id

#RETURN ALL ITEMS FROM THE CURRENT USER'S CART_ID_SESSION_KEY
def get_basket_items(request):
    return Basket.objects.filter(basket_id=_basket_id(request))

def get_songs_count(request):
    items = Basket.objects.filter(basket_id=_basket_id(request))
    return items.count()

def add_to_basket(request):
    postdata = request.POST.copy()
    #GET PRODUCT SLUG FROM POST DATA , RETURN BLANK IF EMPTY
    song_id = postdata.get('song_id','')
    #GET QUANTITY ADDED, RETURN 1 IF EMPTY
    #FETCH THE PRODUCT OR RETURN A MISSING PAGE ERROR
    quantity = postdata.get("qauntity",1)
    music = get_object_or_404(Music, pk=int(song_id)) 
    #GET PRODUCTS IN CART_ID_SESSION_KEY
    basket_music = get_basket_items(request)
    music_in_basket = False
    #CHECK TO SEE IF ITEM IS ALREADY IN CART_ID_SESSION_KEY
    for basket_item in basket_music:
        if basket_item.song.pk == music.id:
            music_in_basket=True
    if not music_in_basket:
        basket = Basket()
        basket.song = music
        basket.quantity = quantity 
        basket.basket_id = _basket_id(request)
        basket.save()

def basket_distinct_item_count(request):
    return get_basket_items(request).count()

def get_single_item(request, item_id):
    return get_object_or_404(Basket, pk=item_id, basket_id=_basket_id(request))

#REMOVE A SINGLE ITEM FROM CART_ID_SESSION_KEY
def remove_from_basket(request):
    postdata = request.POST.copy()
    song_id = postdata['song_id']
    basket_item = get_single_item(request, song_id)
    if basket_item:
        basket_item.delete()

#GETS THE TOTAL COST FOR THE CURRENT CART_ID_SESSION_KEY
def basket_subtotal(request):
    basket_total = decimal.Decimal('0.00')
    basket_songs = get_basket_items(request)
    for basket_song in basket_songs:
        basket_total += basket_song.price
    return basket_total

def is_empty(request):
    return basket_distinct_item_count(request) == 0

def empty_basket(request):
    user_basket = get_basket_items(request)
    user_basket.delete()


def get_songs_in_zip(order):
    sort_order = order.orderline_set.all().order_by("-pk")
    get_songs_pk = [str(pk.songs_pk.pk) for pk in sort_order]
    full_path = settings.PROJECT_ROOT+"/media/music/zips/"+"_".join(get_songs_pk)+".zip"
    if os.path.exists(full_path):
        return full_path
    else:
        zip = zipfile.ZipFile(settings.PROJECT_ROOT+"/media/music/zips/"+"_".join(get_songs_pk)+".zip","w")
        for music in sort_order:
            zip.write(music.songs_pk.full_track.path,music.songs_pk.full_name+".mp3",zipfile.ZIP_DEFLATED)
        zip.close()
        return zip.filename

def zip_songs(basket):
    sort_order = [song.song.pk for song in basket]
    sort_order.sort()
    get_songs_pk = [str(pk) for pk in sort_order]
    
    full_path = settings.PROJECT_ROOT+"/media/music/zips/"+"_".join(get_songs_pk)+".zip"
    if os.path.exists(full_path):
        return
    else:
        zip = zipfile.ZipFile(settings.PROJECT_ROOT+"/media/music/zips/"+"_".join(get_songs_pk)+".zip","w")
        for music in basket:
            zip.write(music.song.full_track.path, music.song.full_name+".mp3",zipfile.ZIP_DEFLATED)
        zip.close()
        return
