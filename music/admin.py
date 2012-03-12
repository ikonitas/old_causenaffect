from django.contrib import admin
from music.models import Music
from music.models import Category

class MusicAdmin(admin.ModelAdmin):
    list_display = ('full_name','songs_order','price',)
    list_editable = ('songs_order',)
admin.site.register(Music, MusicAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',),}

admin.site.register(Category, CategoryAdmin)
