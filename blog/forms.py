from django import forms
from blog.models import Entry
from django.forms import ValidationError

class EntryAdminForm(forms.ModelForm):
    class Meta:
        models = Entry

    #def clean(self):
    #    import ipdb; ipdb.set_trace()
    #    cleaned_data = super(EntryAdminForm, self).clean()
    #    basewidth = 525
    #    image = self.cleaned_data['image']
    #    if image.width < basewidth:
    #        raise ValidationError("Image width size mus be bigger than 525px")
