from django.db import models
from PIL import  Image
from django.contrib.auth.models import User
import os
import datetime
from django.core.validators import MaxLengthValidator
import twitter
from django.conf import settings

class Event(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
            (LIVE_STATUS,'Live'),
            (DRAFT_STATUS,'Draft'),
            )
    title = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True, default=datetime.datetime.now())
    event_date = models.DateField(default=datetime.datetime.now(), help_text="What date is event?")
    time = models.TimeField(help_text="Event time start?")
    price = models.CharField(max_length=10, help_text="Please provide a price withou &#163; sign")
    flayer = models.ImageField(upload_to="uploads/", blank=True, null=True)
    flayer_thumb = models.ImageField(upload_to="thumbs/",blank=True, null=True, editable=False)
    body = models.TextField(validators=[MaxLengthValidator(230)],help_text="Please write more about event")
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    slug = models.SlugField(help_text="Slug is auto generated from title so do not touch", unique=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    def save(self, *args, **kwargs):
        #Twitter APP
        if self.pk is not None:
            orig = Event.objects.get(pk=self.pk)
            if orig.title != self.title:
                ##FACEBOOK
                #fb = facebook.Facebook(settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY)
                #fb.session_key=settings.FACEBOOK_SESSION_KEY
                #fb.status.set(self.title + " " + self.get_full_url())
                
                #TWITTER
                api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, consumer_secret=settings.TWITTER_CONSUMER_SECRET, access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
                api.PostUpdate(self.title +" " + self.get_full_url() )

        elif self.pk is None:
            #FACEBOOK
            #fb = facebook.Facebook(settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY) 
            #fb.session_key=settings.FACEBOOK_SESSION_KEY                                    
            #fb.status.set(self.title + " " + self.get_full_url())                                       #TWITTER
            api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, consumer_secret=settings.TWITTER_CONSUMER_SECRET, access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
            api.PostUpdate("NEW EVENT   " + self.title +" " + self.get_full_url() )
                
        #Flayer resizing image
        super(Event, self).save()
        size = (120,120)
        if not self.flayer:
            return
        if not self.id and not self.flayer:
            return

        try:
            old_obj = Event.objects.get(pk=self.id)
            old_path = old_obj.flayer.path
        except:
            pass

        thumb_update = False
        if self.flayer_thumb:
            try:
                statinfo1 = os.stat(self.flayer.path)
                statinfo2 = os.stat(self.flayer_thumb.path)
                if statinfo1 > statinfo2:
                    thumb_update = True
            except:
                thumb_update = True

        pw = self.flayer.width
        ph = self.flayer.height
        nw = size[0]
        nh = size[1]

        if self.flayer and not self.flayer_thumb or thumb_update:
            # only do this if the image needs resizing
            if (pw, ph) != (nw, nh):
                filename = str(self.flayer.path)
                image = Image.open(filename)
                pr = float(pw) / float(ph)
                nr = float(nw) / float(nh)

                if image.mode not in ('L', 'RGB'):
                    image = image.convert('RGB')

                if pr > nr:
                    # photo aspect is wider than destination ratio
                    tw = int(round(nh * pr))
                    image = image.resize((tw, nh), Image.ANTIALIAS)
                    l = int(round(( tw - nw ) / 2.0))
                    image = image.resize((nw, nh), Image.ANTIALIAS)
                    #image = image.crop((l, 0, l + nw, nh))
                elif pr < nr:
                    # photo aspect is taller than destination ratio
                    th = int(round(nw / pr))
                    image = image.resize((nw, th), Image.ANTIALIAS)
                    t = int(round(( th - nh ) / 2.0))
                    #image = image.crop((0, t, nw, t + nh))
                    image = image.resize((nw, nh), Image.ANTIALIAS)
                else:
                    # photo aspect matches the destination ratio
                    image = image.resize(size, Image.ANTIALIAS)

                image.save(self.get_thumbnail_path())
                (a, b) = os.path.split(self.flayer.name)
                self.flayer_thumb = a + '/thumbs/' + b
                super(Event, self).save()
    
    def get_thumbnail_path(self):
        (head, tail) = os.path.split(self.flayer.path)
        if not os.path.isdir(head + '/thumbs'):
            os.mkdir(head + '/thumbs')
        return head + '/thumbs/' + tail
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-event_date']

    def get_absolute_url(self):
        return "/events/{0}".format(self.slug)

    def get_full_url(self):
        return "http://www.cause-affect.co.uk/events/{0}".format(self.slug)

    def __unicode__(self):
        return self.title
