from django.shortcuts import render_to_response
from django.template import RequestContext
from basket import utils
from orders import utils as orders_utils
from django.http import HttpResponseRedirect
from orders.models import Order
from basket import paypal
from django.http import HttpResponse
from django.conf import settings
from djpjax import pjax
from django.template.response import TemplateResponse

@pjax("pjax/view_basket_pjax.html")
def show_basket(request):
    if request.method == "POST":
        postdata = request.POST.copy()
        if postdata['submit'] == "Remove":
            utils.remove_from_basket(request)
        if postdata['submit'] == "CheckoutPaypal":
            return HttpResponseRedirect("/events/")
    
    basket_items = utils.get_basket_items(request)
    basket_subtotal = utils.basket_subtotal(request)
    
    return TemplateResponse(request, "basket/view_basket.html", {'basket_items':basket_items,'basket_subtotal':basket_subtotal,'paypal_url':settings.PAYPAL_URL,'paypal_email':settings.PAYPAL_EMAIL,'paypal_return_url':settings.PAYPAL_RETURN_URL})


def purchased(request):
    if request.REQUEST.has_key('tx'):
      tx = request.REQUEST['tx']
      try:
        existing = Order.objects.get(tx=tx)
        return render_to_response('basket/error.html', { 'error': "Duplicate transaction" },                  context_instance=RequestContext(request) )
      except Order.DoesNotExist:
        result = paypal.Verify(tx)
        payer_email = result.email()
        payer_full_name = result.full_name()
        basket = utils.get_basket_items(request)
        order = orders_utils.create_order(basket,tx, payer_email, payer_full_name)
        if result.success() and order.total == result.amount(): # valid
            empty_basket = utils.empty_basket(request)
            get_zip = utils.get_songs_in_zip(order)
            with open(get_zip, 'rb') as f:
                response = HttpResponse(f.read())
            response['Content-Type'] = "application/octet-stream";
            response['Content-Disposition'] = "attachment; filename= %s.zip" % str(order)

            return response
        else: # didn't validate
          return render_to_response('basket/error.html', { 'error': "Failed to validate payment" },              context_instance=RequestContext(request) )
    else: # no tx
      return render_to_response('basket/error.html', { 'error': "No transaction specified" },                    context_instance=RequestContext(request) )        
