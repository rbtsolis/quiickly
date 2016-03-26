from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['quiickly.co','149.56.14.136']

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
        'NAME': dirname(join(BASE_DIR, 'db.sqlite3')),
    }
}


'''

Static files configurations on Amazon S3

'''
AWS_STORAGE_BUCKET_NAME = 'quiickly'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJ6WKK6Q33RGKRYWA'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'https://s3.amazonaws.com/quiickly/'

STATIC_ROOT = '/static/'

STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


'''

Media Files for production on Amazon Web Services S3

'''
MEDIA_URL = 'https://s3.amazonaws.com/quiickly/media/'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'quiickly.storages.MediaStorage'
