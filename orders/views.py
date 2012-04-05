from orders.models import Order
from django.shortcuts import render_to_response
from django.template import RequestContext
from paypal.standard.ipn.models import PayPalIPN
from basket import utils
from django.http import HttpResponse
from django.http import Http404
from music.models import Music
from django.views.decorators.csrf import csrf_exempt
import simplejson
from orders.models import OrderLine
from django.contrib.auth.decorators import login_required


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

@csrf_exempt
def download_order(request, order_pk):
    if request.is_ajax():
        try: 
            order = Order.objects.get(pk=order_pk)
            PayPalIPN.objects.get(invoice=order_pk)
            if request.session['cart_id'] == order.basket_id:
                return HttpResponse(simplejson.dumps({"status":"completed"}), mimetype="text/javascript")
        except:
            return HttpResponse(simplejson.dumps({"status":"uncompleted"}), mimetype="text/javascript")
    try:
        basket_nr = request.session['cart_id']
    except:
        raise Http404
    try:
        order = Order.objects.get(pk=order_pk)
    except:
        raise Http404
    try:
        invoice = PayPalIPN.objects.get(invoice=order.pk)
    except:
        order = Order.objects.get(pk=order_pk)
        return render_to_response('orders/download_order.html', {"status":"We are waiting for confirmation of payment for this order.Please wait or try refresh browser with F5...","order":order},context_instance=RequestContext(request))
    if basket_nr == order.basket_id:
        empty_basket = utils.empty_basket(request)
        order.transaction_id = invoice.txn_id
        order.payer_email = invoice.payer_email
        order.payer_full_name = invoice.first_name + " " + invoice.last_name
        order.payment_status = invoice.payment_status
        order.save()
        
        songs = order.orderline_set.all()
        return render_to_response('orders/download_order.html', {'order':order,'songs':songs}, context_instance=RequestContext(request))
    else:

        return render_to_response('orders/download_order.html', {"status":"We are waiting for confirmation of payment for this order.Please wait or try to refresh browser F5...","order":order}, context_instance=RequestContext(request))

@login_required(login_url="/accounts/login")
def download(request, orderline_pk, song_pk):
    orderline = OrderLine.objects.get(pk=orderline_pk)
    song = Music.objects.get(pk=song_pk)
    if orderline.order.user == request.user:
        song = Music.objects.get(pk=orderline.songs_pk_id)
        with open(song.full_track.path, 'rb') as f:
            response = HttpResponse(f.read())
        response['Content-Type'] = "audio/mpeg3"
        response["Content-Disposition"] = "attachment; filename = %s.mp3" % str(song.full_name)
        return response
    else:
        raise Http404
