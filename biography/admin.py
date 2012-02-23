from django.contrib import admin
from biography.models import Biography
from django.forms import Textarea
from django.db import models

class BiographyAdmin(admin.ModelAdmin):
    formfield_overrides = {
            models.TextField:{'widget':Textarea(attrs={'rows':40,'cols':100})},}

    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js',
              '/media/js/tiny_mce/textareas.js',)

admin.site.register(Biography, BiographyAdmin)
