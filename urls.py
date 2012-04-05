from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from core.ajax_views import archive
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="enter.html"), name="home"),
    url(r'^events/', include('events.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^gallery/',include('photologue.urls')),
    url(r'^contact/', include('contacts.urls')),
    url(r'^biography/', include('biography.urls')),
    url(r'^admin/', include('admin_urls')),
    url(r'^archive/$', archive),
    url(r'^order/', include('orders.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('accounts.urls')),
)

urlpatterns += patterns('paypal.standard.ipn.views',
        url(r'^notifying/$', 'ipn', name="paypal-ipn"),
        )

if settings.HOSTNAME == "ed":
    urlpatterns += patterns('',
            (r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT,'show_indexes':True}),
            )
