from django.db import models
import datetime
from django.contrib.auth.models import User
from PIL import Image
import os
from django.forms import ValidationError
from django.conf import settings
import twitter
import facebook

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    STATUS_CHOICES = (
            (LIVE_STATUS,'Live'),
            (DRAFT_STATUS,'Draft'),
            )

    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    image = models.ImageField(upload_to="blog/",blank=True, null=True, help_text="Image field width size must be bigger than 525px")
    image_blog = models.ImageField(upload_to="blog/",blank=True, null=True, editable=False) 
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    slug = models.SlugField(unique_for_date="pub_date")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)

    def clean(self):
        basewidth = 525
        if not self.image:
            return
        if not self.id and not self.image:
            return
        try:
            old_obj = Entry.objects.get(pk=self.id)
        except:
            pass
        pw = self.image.width
        if self.image:
            if pw < basewidth:
                raise ValidationError("Image field width size must be bigger than 525px")
        return


    def save(self, *args, **kwargs):
        #Twitter APP
        if self.pk is not None:
            orig = Entry.objects.get(pk=self.pk)
            if orig.title != self.title:
                #FACEBOOK
                fb = facebook.Facebook(settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY)
                fb.session_key=settings.FACEBOOK_SESSION_KEY
                fb.status.set(self.title + " " + self.get_full_url())
                
                #TWITTER
                api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, consumer_secret=settings.TWITTER_CONSUMER_SECRET, access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
                api.PostUpdate(self.title +" " + self.get_full_url() )

        elif self.pk is None:
            #FACEBOOK
            fb = facebook.Facebook(settings.FACEBOOK_API_KEY, settings.FACEBOOK_SECRET_KEY) 
            fb.session_key=settings.FACEBOOK_SESSION_KEY                                    
            fb.status.set(self.title + " " + self.get_full_url())                                       #TWITTER
            api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, consumer_secret=settings.TWITTER_CONSUMER_SECRET, access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY, access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
            api.PostUpdate("NEW EVENT   " + self.title +" " + self.get_full_url() )

        #IMAGE RESIZING
        super(Entry, self).save()
        basewidth = 525
        if not self.image:
            return
        if not self.id and not self.image:
            return
        try:
            old_obj = Entry.objects.get(pk=self.id)
        except:
            pass
        blog_image_update = False

        if self.image_blog:
            try:
                statinfo1 = os.stat(self.image.path)
                statinfo2 = os.stat(self.image_blog.path)
                if statinfo1 > statinfo2:
                    blog_image_update = True
            except:
                blog_image_update = True
        
        if not self.image:
            self.image_blog.delete()

        if self.image and not self.image_blog or blog_image_update:

            filename = str(self.image.path)
            image = Image.open(filename)
            wpercent = (basewidth / float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image = image.resize((basewidth, hsize), Image.ANTIALIAS)

            image.save(self.get_image_blog_path())
            (a,b) = os.path.split(self.image.name)
            self.image_blog = a + '/blog_images/' + b
            super(Entry, self).save()

    def get_image_blog_path(self):
        (head, tail) = os.path.split(self.image.path)
        if not os.path.isdir(head + "/blog_images"):
            os.mkdir(head + "/blog_images")
        return head + "/blog_images/" + tail
    
    
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return "/blog/{0}".format(self.slug)

    def get_full_url(self):
        return "http://www.cause-affect.co.uk/blog/{0}".format(self.slug)

    def __unicode__(self):
        return self.title
