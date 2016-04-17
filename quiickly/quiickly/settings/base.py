"""
Django settings for quiickly project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from os.path import dirname, abspath, join
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))


ADMINS = (
    ('Roberth Solís', 'roberth.solis@gmail.com'),
    ('Roberth Quiickly', 'roberth@quiickly.co'),
)

# This is when the project have a broken or high error
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-MANAGERS
MANAGERS = (
    ('Roberth Solís', 'roberth.solis@gmail.com'),
    ('Roberth Quiickly', 'roberth@quiickly.co'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#06@m&d08pz&ean+5jx1v7jc=-b6fyf(fom!w6754xc46yed19'


LOCAL_APPS = [
    'apps.orders.apps.OrdersConfig',
    'apps.users',
    'apps.products',
    'apps.web',
    'apps.drugstores',
    'apps.store.apps.StoreConfig',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'social.apps.django_app.default',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]

# Application definition
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quiickly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'quiickly.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = False

USE_TZ = False


'''
Auth Users Configuraation

'''
AUTH_USER_MODEL = 'users.User'

THUMBNAIL_EXTENSION = 'png'



'''
Django Rest Framework Configuration Section

'''
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}



'''
Email Configuration Section

'''
DEFAULT_FROM_EMAIL = 'soporte@quiickly.co'
SERVER_EMAIL = 'soporte@quiickly.co'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@mg.script.com.co'
EMAIL_HOST_PASSWORD = '6fd3925f846edea26cf220bff91db202'
EMAIL_PORT = 587
SUPPORT_EMAIL = 'soporte@quiickly.co'
EMAIL_SUBJECT_PREFIX = '[Quiickly]'


'''
Push Notifications Section

'''
PUSH_NOTIFICATIONS_SETTINGS = {
    "GCM_API_KEY": "AIzaSyA851MR_xbuFkKhRgCdh6R5lrl0H9MWfXk",
}



'''
Django Cors Header Configuration Section

'''
CORS_URLS_REGEX = r'^/api/v1/.*$'

CORS_ALLOW_METHODS = [
    'GET',
]
