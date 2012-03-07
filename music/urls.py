from django.conf.urls.defaults import patterns, include, url
from music.views import music
from music.views import categories_songs
from basket.views import show_basket

urlpatterns = patterns('',
        url(r'^$', music, name="music"),
        url(r'^(?P<slug>[\w\-]+)/$', categories_songs, name="categories_songs"),
        url(r'^cart/$',show_basket, name="cart"),

        )
