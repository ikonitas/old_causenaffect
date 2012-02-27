from django.db import models
from PIL import  Image
import os


class Music(models.Model):
    full_track = models.FileField(upload_to="music/")
    track_sample = models.FileField(upload_to="music/samples")
    artist = models.CharField(default="Cause N Affect", max_length=50)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="music/images", blank=True, null=True)

    def __unicode__(self):
        return "{0} - {1}".format(self.artist, self.title)

    def save(self, *args, **kwargs):
        super(Music, self).save()
        size = (38,38)
        if not self.image:
            return
        if not self.id and not self.image:
            return
        try:
            old_obj = Music.objects.get(pk=self.id)
            old_path = old_obj.image.path
        except:
            pass

        pw = self.image.width
        ph = self.image.height
        nw = size[0]
        nh = size[1]

        if self.image:
            # only do this if the image needs resizing
            if (pw, ph) != (nw, nh):
                filename = str(self.image.path)
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
                (a, b) = os.path.split(self.image.name)
                self.image = a + '/thumbs/' + b
                super(Music, self).save()

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


