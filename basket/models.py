from django.db import models
from music.models import Music

class Basket(models.Model):
    basket_id = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    song  = models.ForeignKey(Music,related_name="song")

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
        return self.basket_id

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()
