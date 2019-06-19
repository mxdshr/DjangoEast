from .base import *

DEBUG = False

# 替换成你的域名
ALLOWED_HOSTS = ['www.eastnotes.com', 'eastnotes.com']

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


