from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.forms import UserProfileForm
from orders.models import Order
from paypal.standard.ipn.models import PayPalIPN
from basket import utils

def register(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password1'])
            user.save()
            userp = UserProfile(user=user)
            userp.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password2'])
            login(request, new_user)
            return HttpResponseRedirect("/events/")

    else:
        form = UserProfileForm()
    return render_to_response("accounts/register.html", {'form':form },context_instance=RequestContext(request))

def logoug_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def profile(request):
    user= request.user
    orders = Order.objects.filter(user=user)
    user_orders = []
    for order in orders:
        try:
            invoice = PayPalIPN.objects.get(invoice=order.pk)
            if invoice:
                empty_basket = utils.empty_basket(request)
                order.transaction_id = invoice.txn_id
                order.payer_email = invoice.payer_email
                order.payer_full_name = invoice.first_name + " " + invoice.last_name
                order.payment_status = invoice.payment_status
                order.save()
                user_orders.append(order)
        except: 
            pass
    user_songs = []
    if user_orders:
        for order in user_orders:
            songs = order.orderline_set.all()
            user_songs.append(songs)
    
    return render_to_response("accounts/profile.html",{'orders':orders,'user_orders':user_orders,'orderlines':user_songs},context_instance=RequestContext(request))
