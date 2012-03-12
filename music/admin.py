from django.contrib import admin
from music.models import Music
from music.models import Category

class MusicAdmin(admin.ModelAdmin):
    list_display = ('full_name','category','songs_order','price',)
    list_editable = ('songs_order',)
admin.site.register(Music, MusicAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','order',)
    list_editable = ('order',)
    prepopulated_fields = {'slug':('title',),}

admin.site.register(Category, CategoryAdmin)
