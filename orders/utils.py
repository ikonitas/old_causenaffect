from orders.models import Order
from orders.models import OrderLine

def create_order(request,basket):
    subtotal = 0
    for song_price in basket:
        subtotal += song_price.song.price
    if subtotal == 0:
        return

    order = Order()
    order.user = request.user
    order.total = subtotal
    order.basket_id = request.session['cart_id']
    order.save()

    for song in basket:
        line = OrderLine()
        line.order = order
        line.songs_pk_id = song.song.pk
        line.songs_name = song.song.full_name
        line.line_price = song.song.price
        line.save()
    
    return order
