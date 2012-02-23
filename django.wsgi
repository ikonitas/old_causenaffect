import os
import sys

activate_this = os.path.join("/home/ed/Documents/html/Django/kanedj/", "bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

root = os.path.join(os.path.dirname(__file__),'/home/ed/Documents/html/Django/kanedj/')
sys.path.insert(0, root)
sys.path.append("/home/ed/Documents/html/Django/kanedj/kane")
os.environ["DJANGO_SETTINGS_MODULE"] = "kane.settings"

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
