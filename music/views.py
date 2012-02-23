from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from djpjax import pjax

@pjax("pjax/music_pjax.html")
def music(request):
    return TemplateResponse(request, "music/music.html", {'test':'test'})
