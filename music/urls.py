from django.conf.urls.defaults import patterns, include, url
from music.views import music
from basket.views import show_cart

urlpatterns = patterns('',
        url(r'^$', music, name="music"),
        url(r'^cart/$',show_cart, name="cart"),
        )
