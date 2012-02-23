from django.conf.urls.defaults import patterns, include, url
from contacts.views import contact

urlpatterns = patterns('',
    url('^$', contact, name="contact"),
    )
