import os
import sys
import socket

if socket.gethostname() == "ed":
    activate_this = os.path.join("/www/causenaffect/")

    root = os.path.join(os.path.dirname(__file__),"/www/causenaffect")
    sys.path.insert(0, root)
    sys.path.append("/www/causenaffect/causenaffect/")
    sys.path.append("/www/causenaffect/lib/python2.7/site-packages/")
    os.environ["DJANGO_SETTINGS_MODULE"] = "causenaffect.settings"

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()

else:
    activate_this = os.path.join("/www/")
    
    root = os.path.join(os.path.dirname(__file__),'/www')
    sys.path.insert(0, root)
    sys.path.append("/www/causenaffect/")
    os.environ["DJANGO_SETTINGS_MODULE"] = "causenaffect.settings"
    
    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()
