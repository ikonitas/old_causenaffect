from orders.models import Order
from orders.models import OrderLine
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    #def changelist_view(self, request, extra_context=None):
    #    if not request.GET.has_key('payment_status__exact'):
    #        qu = request.GET.copy()
    #        qu['payment_status__exact'] = 'Completed'
    #        request.GET = qu
    #        request.META['QUERY_STRING'] = request.GET.urlencode()
    #    return super(OrderAdmin,self).changelist_view(request, extra_context=extra_context)
    list_display = ('order_number','purchased_at','payment_status','transaction_id','payer_email','payer_full_name','basket_id','total',)

admin.site.register(Order, OrderAdmin)
