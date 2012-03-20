from causenaffect.paypal.standard.forms import PayPalPaymentsForm
from basket import utils
from orders import utils as orders_utils
from django.conf import settings
from djpjax import pjax
from django.template.response import TemplateResponse
from django.conf import settings


@pjax("pjax/view_basket_pjax.html")
def show_basket(request):
    if request.method == "POST":
       postdata = request.POST.copy()
       if postdata['song_id']:
           utils.remove_from_basket(request)
    basket_items = utils.get_basket_items(request)
    basket_subtotal = utils.basket_subtotal(request)
    order = orders_utils.create_order(request, basket_items)
    
    if order:
        paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "return_url": settings.PAYPAL_RETURN_URL + "{0}/".format(order.pk),
        "invoice": "{0}".format(order.pk),               
        "notify_url": settings.PAYPAL_NOTIFY_URL,
        "cancel_return": settings.PAYPAL_CANCEL_RETURN + "{0}/".format(order.pk),
     }

        form = PayPalPaymentsForm(basket_items,initial=paypal_dict)
        
        if settings.SERVER_STATUS == "LIVE":
            form_type = form.render()
        else:
            form_type = form.sandbox()

        return TemplateResponse(request, "basket/view_basket.html", {'basket_items':basket_items,'basket_subtotal':basket_subtotal,'form':form_type})
    
    else:
        return TemplateResponse(request, "basket/view_basket.html", {'basket_items':basket_items,'basket_subtotal':basket_subtotal})
