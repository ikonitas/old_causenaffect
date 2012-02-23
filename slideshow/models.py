from django.db import models
import PIL
import os
from django.forms import ValidationError

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slideshow/")
    image_slide = models.ImageField(upload_to="slideshow/in/", null=True, blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def clean(self):
        size = (272, 182)
        if not self.image:
            return
        if not self.id and not self.image:
            return
        
        pw = self.image.width
        ph = self.image.height
        nw = size[0]
        nh = size[1]
        
        if pw < nw:
            raise ValidationError("Image field width size must be bigger than 272px")
        if ph < nh:
            raise ValidationError("Image field height must be bigger than 182px")
        return


    def save(self, *args, **kwargs):
        size = (272, 182)
        super(Image, self).save()
        if not self.image:
            return
        if not self.id and not self.image:
            return
        try:
            old_obj = Image.objects.get(pk=self.id)
        except:
            pass

        image_slideshow = False
        if self.image_slide:
            try:
                statinfo1 = os.stat(self.image.path)
                statinfo2 = os.stat(self.image_slide.path)
                if statinfo1 > statinfo2:
                    image_slideshow = True
            except:
                image_slideshow = True

        pw = self.image.width
        ph = self.image.height
        nw = size[0]
        nh = size[1]
        
        if self.image and not self.image_slide or image_slideshow:
            if (pw, ph) != (nw, nh):
                filename = str(self.image.path)
                image = PIL.Image.open(filename)
                pr = float(pw) / float(ph)
                nr = float(nw) / float(nh)

                if image.mode not in ("L","RGB"):
                    image = image.convert("RGB")

                if pr > nr:
                    tw = int(round(nh * pr))
                    image = image.resize((tw, nh), PIL.Image.ANTIALIAS)
                    l = int(round(( tw - nw) / 2.0))
                    image = image.crop((l, 0, l + nw, nh))
                elif pr < nr:
                    th = int(round(nw /pr))
                    image = image.resize((nw, th), PIL.Image.ANTIALIAS)
                    t = int(round(( th - nh ) / 2.0))
                    image = image.crop((0, t, nw, t + nh))
                else:
                    image = image.resize(size, PIL.Image.ANTIALIAS)

            image = image.convert("RGB")
            image.save(self.get_thumbnail_path(),'JPEG',)
            (a, b) = os.path.split(self.image.name)
            (name, end) = b.split('.')
            self.image_slide = a + '/slide/' + name + ".jpg"
            super(Image, self).save()
    
    def get_thumbnail_path(self):
        (head, tail) = os.path.split(self.image.path)
        (name, end) = tail.split('.')
        if not os.path.isdir(head + "/slide"):
            os.mkdir(head + "/slide")
        return head + "/slide/" + name + ".jpg"


    

    def admin_thumbnail(self):
        return u'<img src="%s" height=120 width=120 />' % self.image_slide.url
    admin_thumbnail.short_description = "Image"
    admin_thumbnail.allow_tags = True
