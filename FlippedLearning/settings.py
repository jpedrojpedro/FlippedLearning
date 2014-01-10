#encoding: utf-8
# Django settings for Flipped Learning project.
from os import environ
import os

PROJECT_DIR = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('João Pedro Pinheiro', 'joaopedro.pinheiro88@gmail.com'),
)

MANAGERS = ADMINS

"""
How to fill DATABASES Dictionary:
Engine => 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
Name => Schema name or if it is SQLite, use the full path including filename
User => Username with privileges in database or empty if it is SQLite
Password => Password from the used User above or empty if it is SQLite
Host => Server ip where your database is running or empty if it is SQLite
Port => 5432, 3306, 1537
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ.get("DB_SCHEMA", "flipped_learning"),
        'USER': environ.get("DB_USER", "jpedro"),
        'PASSWORD': environ.get("DB_PWD", "102030jp"),
        'HOST': environ.get("DB_HOST", "127.0.0.1"),
        'PORT': '5432',
    }
}

"""
Local time zone for this installation.
Choices can be found here:
    http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
Although not all choices may be available on all operating systems.
On Unix systems, a value of None will cause Django to use the same
timezone as the operating system.
If running in a Windows environment this must be set to the same as your
system time zone.
"""

TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-BR'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/inicio"

# Organização de arquivos estáticos
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'static/media/')
STATIC_URL = '/static/collect/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/collect/')
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, 'templates/'),)

STATICFILES_DIRS = (

)
#MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
#MEDIA_URL = '/media/'
#STATIC_ROOT = os.path.join(PROJECT_DIR, 'collect/')
#STATIC_URL = '/collect/'

# URL prefix for admin static files -- css, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(6x+j_$6fpy69^bvgv-hrf(9bgyv&u$(lhn#t-(o)*g=m0uyjv'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'FlippedLearning.urls'

SOCIAL_AUTH_UID_LENGTH = 200

"""
How to fill INSTALLED_APPS tuple:
Here are listed the allowed apps that can in your Django instance.
We add: database_app,
"""

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'database_app',
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID = environ.get("FB_APP_ID", "")
FACEBOOK_API_SECRET = environ.get("FB_APP_KEY", "")

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}