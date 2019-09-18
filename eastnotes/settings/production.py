from .base import *

DEBUG = False
ALLOWED_HOSTS = ['www.eastnotes.com', 'eastnotes.com', '118.89.245.71']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '3306',
        'HOST': 'localhost',
    }
}


