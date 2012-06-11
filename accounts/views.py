import random
import string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth import authenticate 
from django.contrib.auth import login as login_after_registration
from django.contrib.auth.views import login
from django.contrib import messages
from accounts.forms import UserProfileForm
from orders.models import Order
from paypal.standard.ipn.models import PayPalIPN
from basket import utils
from django.contrib.auth.decorators import login_required

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
            login_after_registration(request, new_user)
            return HttpResponseRedirect("/events/")

    else:
        form = UserProfileForm()
    return render_to_response("accounts/register.html", {'form':form },context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url="/accounts/login")
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

def mine_login(request, *args, **kwargs):
    if request.method == "POST":
        if not request.POST.get('remember',None):
            request.session.set_expiry(0)
    return login(request, *args, **kwargs)

def forget(request):
    if request.method == "POST":
        if request.POST.get("email",""):
            try:
                user = UserProfile.objects.get(user__email=request.POST.get('email'))
                new_password = "".join([random.choice(string.letters.lower()) for x in range(7)])
                user.user.set_password(new_password)
                user.user.save()
                send_mail("CAUSENAFFECT your password", "Hi " + user.user.username + " this is your new password: " + new_password, settings.EMAIL_HOST_USER,[user.user.email], fail_silently=True)
                return render_to_response("accounts/failed_email.html", context_instance=RequestContext(request))
            except UserProfile.DoesNotExist:
                error = True
                return render_to_response("accounts/failed_email.html",{'error':error }, context_instance=RequestContext(request))
    else:
        pass
