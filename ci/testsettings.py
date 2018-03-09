# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = False

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cdhweb.db'
    }
}

# required with django 1.11 when debug is false, even for tests
ALLOWED_HOSTS = ["*"]

# configure django-compressor to compress css & javascript
COMPRESS_ENABLED = True

