import os
import sys

activate_this = os.path.join("/www/")

root = os.path.join(os.path.dirname(__file__),'/www')
sys.path.insert(0, root)
sys.path.append("/www/causenaffect/")
os.environ["DJANGO_SETTINGS_MODULE"] = "causenaffect.settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
