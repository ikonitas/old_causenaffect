from django.conf.urls.defaults import patterns, include, url
from blog.views import blog_index
from blog.views import very_archive
from blog.views import entries_months
from blog.views import entries_year
from blog.views import entries_detail

urlpatterns = patterns('',
    url(r'^$',blog_index),
    url(r'^archive/$', very_archive, name="full_archive"),
    url(r'^(?P<year>\d{4})/(?P<month>[-\w]+)/$', entries_months, name="entries_months"),
    url(r'^(?P<year>\d{4})/$', entries_year, name="entries_years"),
    url(r'^(?P<slug>[-\w]+)/', entries_detail, name="entries_detail"),
    )
