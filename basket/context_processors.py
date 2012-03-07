from basket import utils

def basket_items(request):
    songs_count = utils.get_songs_count(request)
    basket_subtotal = utils.basket_subtotal(request)

    return {"songs_count":songs_count, "basket_subtotal":basket_subtotal}
