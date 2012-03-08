from django.template.response import TemplateResponse
from djpjax import pjax
from music.models import Music
from django.shortcuts import get_object_or_404
from music.models import Category

@pjax("pjax/music_pjax.html")
def music(request):
    music_list = Music.objects.all()
    return TemplateResponse(request, "music/music.html", {'music_list':music_list})

@pjax("pjax/songs_pjax.html")
def categories_songs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    songs = Music.objects.all().filter(category=category)
    return TemplateResponse(request, "categories/songs.html",{'songs':songs})
