from orders.models import Order
from django.shortcuts import render_to_response
from django.template import RequestContext

def view_order(request, order_pk):
    order = Order.objects.get(pk=order_pk)

    return render_to_response(
        'admin/orders/view_order.html',
        {
            'order' : order,
            'root_path': '/admin/',
        },
        RequestContext(request)
    )
