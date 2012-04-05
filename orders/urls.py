from django.conf.urls.defaults import patterns, include, url
from orders.views import download


urlpatterns = patterns ('',
    url(r'^(?P<orderline_pk>[\d]+)/(?P<song_pk>[\d]+)/$', download, name="download"),
    )
