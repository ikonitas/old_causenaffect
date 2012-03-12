from django.db import models
from PIL import  Image
import os

class Category(models.Model):
    title = models.CharField(max_length=20)
    date_added = models.DateField(auto_now_add="True",editable=False)
    order = models.IntegerField(null=True, blank=True, unique=True)
    slug = models.SlugField(max_length=20, editable=True, help_text="Please do not edit this field as this field is going to be prepopulated from title")

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/music/"+self.slug

class Music(models.Model):
    full_track = models.FileField(upload_to="music/")
    track_sample = models.FileField(upload_to="music/samples")
    artist = models.CharField(default="Cause N Affect", max_length=50)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    songs_order = models.IntegerField(null=True, blank=True, unique=True)

    class Meta:
        ordering = ('songs_order',)

    def __unicode__(self):
        return "{0} - {1}".format(self.artist, self.title)

    def _full_name(self):
        return self.artist + " - " + self.title
    full_name = property(_full_name)

    def get_thumbnail_path(self):
        (head, tail) = os.path.split(self.image.path)
        if not os.path.isdir(head + '/thumbs'):
            os.mkdir(head + '/thumbs')
        return head + '/thumbs/' + tail

    def get_full_image_path(self):
        (head, tail) = os.path.split(self.image.url)
        head = head.replace("thumbs","")
        return head + tail

    def get_image_name(self):
        (head, tail) =  os.path.split(self.image.name)
        return tail


