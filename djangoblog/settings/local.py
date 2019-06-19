from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_east',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306',
        'HOST': 'localhost',
    }
}

