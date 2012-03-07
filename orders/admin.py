from orders.models import Order
from orders.models import OrderLine
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number','purchased_at','tx','payer_email','payer_full_name','total',)

admin.site.register(Order, OrderAdmin)
