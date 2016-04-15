from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['quiickly.co','www.quiickly.co','149.56.14.136',]


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quiickly2db',
        'USER': 'quiickly2',
        'PASSWORD': 'aistream',
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

Static files configurations on Amazon S3

'''
AWS_STORAGE_BUCKET_NAME = 'quiickly'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJEGN7KTJESC3XGBA'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'https://s3.amazonaws.com/quiickly/static/'

STATIC_ROOT = join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


'''

Media Files for production on Amazon Web Services S3

'''
MEDIA_URL = 'https://s3.amazonaws.com/upstudy/media/'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'quiickly.storages.MediaStorage'
