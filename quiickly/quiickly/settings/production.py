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
AWS_STORAGE_BUCKET_NAME = 'upstudy'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAITEOIGGQ5Z5TIATQ'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'https://s3.amazonaws.com/upstudy/'

STATIC_ROOT = dirname(join(BASE_DIR, 'static'))
print(STATIC_ROOT)

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
