from django.db import models
from music.models import Music

class Order(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=250,null=True, blank=True)
    payer_email = models.EmailField(null=True, blank=True)
    payer_full_name = models.CharField(max_length=100, null=True,blank=True)
    payment_status = models.CharField(max_length=20, null=True, blank=True,default="Uncompleted")
    basket_id= models.CharField(max_length=200, null=True, blank=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)

    def __unicode__(self):
        return "%07d" % self.pk

    def order_number(self):
        return "%07d" % self.pk

class OrderLine(models.Model):
    """Orderline relating to a specific order."""
    order = models.ForeignKey(Order)
    songs_pk = models.ForeignKey(Music)
    songs_name = models.CharField(max_length=255)
    line_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return str(self.pk)
