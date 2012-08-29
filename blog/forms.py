from django import forms
from blog.models import Entry

class EntryAdminForm(forms.ModelForm):
    class Meta:
        models = Entry
