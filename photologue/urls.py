from django.conf import settings
from django.conf.urls.defaults import *
from models import *
from photologue.views import albums

# Number of random images from the gallery to display.
SAMPLE_SIZE = ":%s" % getattr(settings, 'GALLERY_SAMPLE_SIZE', 5)

# galleries
urlpatterns = patterns('',
        url(r'^$', albums, name="albums"),
        )


