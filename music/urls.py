from django.conf.urls.defaults import patterns, include, url
from music.views import music

urlpatterns = patterns('',
        url(r'^$', music, name="music"),
        )
