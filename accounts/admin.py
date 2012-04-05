from django.contrib import admin
from accounts.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_joined','email',)

admin.site.register(UserProfile, UserProfileAdmin)
