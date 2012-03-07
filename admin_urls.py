from django.conf.urls.defaults import *
from orders.views import view_order
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^orders/order/(\d+)/$', view_order),
    (r'', include(admin.site.urls)),
)
