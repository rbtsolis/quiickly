from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['quiickly.co']

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quiicklydbuser',
        'PASSWORD': 'quiicklypassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}


'''

Static and media files configurations

'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

