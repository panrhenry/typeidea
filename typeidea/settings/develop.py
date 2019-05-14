import os
from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'HOST': '192.168.174.132',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
    }
}


