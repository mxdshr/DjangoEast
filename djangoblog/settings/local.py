from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'www_eastnotes_c',
        'USER': 'reborn',
        'PASSWORD': 'asd10000',
        'PORT': '3306',
        'HOST': '118.89.245.71',
    }
}

