from .base import *

DEBUG = False
ALLOWED_HOSTS = ['www.eastnotes.com', 'eastnotes.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'www_eastnotes_c',
        'USER': 'reborn',
        'PASSWORD': 'asd10000',
        'PORT': '3306',
        'HOST': 'localhost',
    }
}


