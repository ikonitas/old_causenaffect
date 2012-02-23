from django.conf.urls.defaults import patterns, include, url
from biography.views import biography_view

urlpatterns = patterns('',
        url(r'^$', biography_view, name="biography"),
        )
