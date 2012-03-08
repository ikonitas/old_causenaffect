# Django settings for kane project.
import socket
import os

HOSTNAME = socket.gethostname()

PROJECT_ROOT = os.path.join(os.path.dirname(__file__).decode('utf-8'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False }

INTERNAL_IPS = ('127.0.0.1',)

APPEND_SLASH = True

ADMINS = (
	("Edvinas Jurevicius", "ikonitas@gmail.com"),
    # ('Your Name', 'your_email@example.com'),
)


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kanedb',                      # Or path to database file if using sqlite3.
        'USER': 'kane',                      # Not used with sqlite3.
        'PASSWORD': 'sidabras',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_ROOT + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_ROOT + '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '9!q+heofz9apm12flb81wl8)o4$b22f@2!^g@)@n9aqddy7rni'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

if socket.gethostname() == "ed":
    ROOT_URLCONF = 'urls'
else:
    ROOT_URLCONF = 'causenaffect.urls'

TEMPLATE_DIRS = (

       PROJECT_ROOT + "/templates/",
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)




TEMPLATE_CONTEXT_PROCESSORS = (
     'django.core.context_processors.debug',
     'django.core.context_processors.i18n',
     'django.core.context_processors.media',
     'django.core.context_processors.static',
     'django.core.context_processors.request',
     'django.contrib.auth.context_processors.auth',
     'django.contrib.messages.context_processors.messages',
     'slideshow.context_processors.images',
     'music.context_processors.categories',
     )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'blog',
    'events',
    'south',
    'pure_pagination',
    'core',
    'filebrowser',
    'contacts',
    'captcha',
    'slideshow',
    'photologue',
    'biography',
    'music',
    #'djpjax',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

PAGINATION_SETTINGS = {
        'PAGE_RANGE_DISPLAYED': 10,
        'MARGIN_PAGES_DISPLAYED': 2,
        }

TINYMCE_JS_URL = MEDIA_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = MEDIA_ROOT + 'js/tiny_mce'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ikonitas@gmail.com'
EMAIL_HOST_PASSWORD = 'sidabras0915'


CAPTCHA_FONT_PATH = PROJECT_ROOT + "/media/fonts/Vera.ttf"
CAPTCHA_FONT_SIZE = 30
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'


TWITTER_CONSUMER_KEY="ExeGepftghGohvlivfI8sA"
TWITTER_CONSUMER_SECRET="4ZGYSPb7IpGEudguiXG6oyXYkizFyYRWyw7WsMjfdQ"
TWITTER_ACCESS_TOKEN_KEY="256521432-O1EyGylV4azeFJRol7rbhaD8C6mr0QGES7oODRi0"
TWITTER_ACCESS_TOKEN_SECRET="mQmhi7Chv3BYsuFWAThwlHhDI7WqhYoixrQEvGf4"

FACEBOOK_API_KEY =  280734208662299
FACEBOOK_SECRET_KEY = "ae2cf8ac0b4056af62caa0d98d3a2785"
FACEBOOK_SESSION_KEY = u'2.AQCao5OXnhlQd1VS.3600.1329955200.0-100000009533032'
