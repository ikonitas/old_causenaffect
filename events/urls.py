from django.conf.urls.defaults import patterns, include, url
from events.views import index_view
from events.views import event_detail
from events.views import events_years
from events.views import events_months
from events.views import very_archive
urlpatterns = patterns('',
    url(r'^$', index_view, name="events_view"),
    url(r'^archive/$',very_archive, name="full_archive"), 
    url(r'^(?P<year>\d{4})/(?P<month>[-\w]+)/$',events_months, name="events_months"),
    url(r'^(?P<year>\d{4})/$', events_years, name="events_years"),
    url(r'^(?P<slug>[-\w]+)/', event_detail, name="event_detail"),

    )
