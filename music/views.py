from django.template.response import TemplateResponse
from djpjax import pjax
from music.models import Music
from django.shortcuts import get_object_or_404
from music.models import Category
from django.http import HttpResponse
from basket import utils
import simplejson

@pjax("pjax/music_pjax.html")
def music(request):
    music_list = Music.objects.all()
    if request.method == "POST":
        utils.add_to_basket(request)
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        basket_count_songs = utils.get_songs_count(request)
        basket_subtotal = utils.basket_subtotal(request)
        return HttpResponse(simplejson.dumps({"basket_count_songs":basket_count_songs,"basket_subtotal":"%.2f" % basket_subtotal}), mimetype="text/javascript")
    else:
        music_list = Music.objects.all()
    request.session.set_test_cookie()
    basket_count_songs=utils.get_songs_count(request)
    basket_subtotal = utils.basket_subtotal(request)
    return TemplateResponse(request, "music/music.html", {'music_list':music_list,"basket_count_songs":basket_count_songs,"basket_subtotal":basket_subtotal})

@pjax("pjax/songs_pjax.html")
def categories_songs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    songs = Music.objects.all().filter(category=category)
    return TemplateResponse(request, "categories/songs.html",{'songs':songs})
