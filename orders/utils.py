from orders.models import Order
from orders.models import OrderLine

def create_order(basket, tx, payer_email, payer_full_name):
    subtotal = 0
    for song_price in basket:
        subtotal += song_price.song.price

    order = Order()
    order.tx = tx
    order.total = subtotal
    order.payer_email = payer_email
    order.payer_full_name = payer_full_name
    order.save()

    for song in basket:
        line = OrderLine()
        line.order = order
        line.songs_pk_id = song.song.pk
        line.songs_name = song.song.full_name
        line.line_price = song.song.price
        line.save()
    
    return order
