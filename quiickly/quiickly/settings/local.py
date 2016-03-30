from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'debug_toolbar.apps.DebugToolbarConfig',
]


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}


'''

Static files configurations

'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')


'''
Thumbnail Configuration Section

'''
# Show thumbnail generation errors
THUMBNAIL_DEBUG = True
