from django.contrib import admin
from events.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','time','price',)
    prepopulated_fields = {"slug":("title",)}
    
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js',
              '/media/js/tiny_mce/textareas.js',)

admin.site.register(Event, EventAdmin)
