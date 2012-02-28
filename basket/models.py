from django.db import models
from music.models import Music

class BasketItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    song  = models.ForeignKey('music.music', unique=True)

    class Meta:
        ordering = ['date_added']

    @property
    def total(self):
        return self.quantity * self.song.price

    @property
    def name(self):
        return self.song.artist + " - " + self.song.title

    @property
    def price(self):
        return self.song.price

    def __unicode__(self):
        return self.cart_id

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

