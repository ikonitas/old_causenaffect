from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))
    captcha= CaptchaField()

def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    self.fields['name'].widget.attrs['class'] = 'gaodynas'
