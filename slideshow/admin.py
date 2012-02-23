from django.contrib import admin
from slideshow.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "admin_thumbnail", "is_active")
    list_editable = ("is_active",)

admin.site.register(Image, ImageAdmin)
