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
