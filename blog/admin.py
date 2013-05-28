from django.contrib import admin
from blog.models import Entry
from blog.forms import EntryAdminForm

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    form = EntryAdminForm

    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js',
              '/media/js/tiny_mce/textareas.js',)

admin.site.register(Entry, EntryAdmin)
