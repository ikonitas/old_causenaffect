from contacts.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from djpjax import pjax
from django.template.response import TemplateResponse
from django.conf import settings

@pjax("pjax/contact_pjax.html")
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            human = True
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipients = [settings.EMAIL_HOST_USER]

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
            return HttpResponse("thanks");
    else:
        form = ContactForm()

    return TemplateResponse(request, "contacts/contact.html",{'form':form})
