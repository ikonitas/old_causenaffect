from contacts.forms import ContactForm
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.context import RequestContext
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from captcha.fields import CaptchaField
from djpjax import pjax
from django.template.response import TemplateResponse

@pjax("contact_pjax.html")
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            human = True
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = ['ikonitas@gmail.com']

            plaintext = get_template('contacts/email.txt')
            d = Context({'name':name,
                         'email':email,
                         'subject':subject,
                         'message':message})
            subject, from_email, to = subject, email, recipients
            text_content = plaintext.render(d)
            headers = {'Reply-To': email}
            msg = EmailMultiAlternatives(subject,text_content, from_email,to, headers=headers)
            msg.send()
            return HttpResponseRedirect("/thanks/")
    else:
        form = ContactForm()

    return TemplateResponse(request, "contacts/contact.html",{'form':form})
#render_to_response('contacts/contact.html', {
#        'form':form,}, context_instance=RequestContext(request))
