from django.template.response import TemplateResponse
from djpjax import pjax
from music.models import Music
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

@pjax("pjax/music_pjax.html")
def music(request):
    music_list = Music.objects.all()
    return TemplateResponse(request, "music/music.html", {'music_list':music_list})

def play(request, song_title):
    music = get_object_or_404(Music, title=song_title)
    path = music.track_sample.path
    response = HttpResponse(music.track_sample.url)
    #response['Content-Disposition'] = 'attachment; filename='+path
    response['Content-Type'] = "audio/mpeg"
    #response['Content-Disposition'] = "attachment; filename= %s - %s.mp3" % (music.artist, music.title)
    return response
