from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserProfileForm(forms.Form):
    username = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=30, label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        try:
            user = User.objects.get(email=email)
            if user is not None:
                raise forms.ValidationError(
                    'This e-mail address is already registered with this site.'
                )
        except User.DoesNotExist:
            pass
        return email
