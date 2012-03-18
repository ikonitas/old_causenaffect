from django.conf.urls.defaults import patterns, include, url
from orders.views import download_order
from orders.views import download


urlpatterns = patterns ('',
    url(r'^(?P<order_pk>[\d]+)/$', download_order, name="download_order"),
    url(r'^(?P<order_pk>[\d]+)/(?P<song_pk>[\d]+)/$', download, name="download"),
    )
