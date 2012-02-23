from django.db import models

class Biography(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __unicode__(self):
        return self.title
