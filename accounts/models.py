from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)


    def date_joined(self):
        return self.user.date_joined

    def email(self):
        return self.user.email
