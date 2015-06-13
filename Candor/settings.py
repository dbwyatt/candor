"""
Django settings for Candor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Set the environment
ENVIRONMENT = 'dev'
if os.path.dirname(BASE_DIR) == '/var/www/candor':
    ENVIRONMENT = 'production'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w58yt2*jmvxdwh-n3o*nf66#4+rl6^5172o&)gx69t04(5*8ow'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if ENVIRONMENT == 'dev':
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '.candorcontracts.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus.controller',
    'homepage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mako_plus.controller.router.RequestInitMiddleware',
)

ROOT_URLCONF = 'Candor.urls'

WSGI_APPLICATION = 'Candor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {}
if ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'candor',
            'USER': 'postgres',
            'PASSWORD': 'Candorthis@db',
            'HOST': '162.243.150.208',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'candordev',
            'USER': 'postgres',
            'PASSWORD': 'Candorthis@db',
            'HOST': '162.243.150.208',
            'PORT': '5432',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

###############################################################
# Specific settings for the Django-Mako-Plus app

DJANGO_MAKO_PLUS = {
    # identifies where the Mako template cache will be stored,
    # relative to each app
    'TEMPLATES_CACHE_DIR': 'cached_templates',

    # the default app and page to render in Mako when the url is too short
    'DEFAULT_PAGE': 'index',
    'DEFAULT_APP': 'homepage',

    # the default encoding of template files
    'DEFAULT_TEMPLATE_ENCODING': 'utf-8',

    # these are included in every template by default - if you put your most-used libraries here, you won't have to import them exlicitly in templates
    'DEFAULT_TEMPLATE_IMPORTS': [
        'import os, os.path, re, json',
    ],

    # see the DMP online tutorial for information about this setting
    'URL_START_INDEX': 0,

    # whether to send the custom DMP signals -- set to False for a slight speed-up in router processing
    # determines whether DMP will send its custom signals during the process
    'SIGNALS': True,

    # whether to minify using rjsmin, rcssmin during 1) collection of static files, and 2) on the fly as .jsm and .cssm files are rendered
    # rjsmin and rcssmin are fast enough that doing it on the fly can be done without slowing requests down
    'MINIFY_JS_CSS': True,

    # see the DMP online tutorial for information about this setting
    'TEMPLATES_DIRS': [
        # '/var/somewhere/templates/',
    ],
}

#  End of settings for the Django-Mako-Plus
################################################################
