

import os
import sys

import dj_database_url
import envdir


def root(*args):
    file_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(file_path, '..', '..', *args))

sys.path.append(root('apps'))

env = root('deploy', 'env')
if os.path.exists(env):
    with open(env, 'r') as f:
        env = f.read().strip()
else:
    # default to dev environment
    env = 'development'

envdir.open(root('deploy', env))

DEBUG = 'DJANGO_DEBUG' in os.environ
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')

if 'ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = [
        host.strip() for host in os.environ['ALLOWED_HOSTS'].split(',')
    ]
else:
    ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'easy_thumbnails',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

###
### Databases
###
DATABASES = {'default': dj_database_url.config()}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'

USE_I18N = False
USE_L10N = False
USE_TZ = True

###
### Static and Media
###
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', root('media'))

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT', '')

STATICFILES_DIRS = (
    root('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'styles/main.less',
        ),
        'output_filename': 'styles/main.css',
    },
}

###
### Templates
###
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    )

TEMPLATE_DIRS = (
    root('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
)

###
### Build
###
if '_BUILD_NUMBER' in os.environ:
    BUILD_NUMBER = os.environ['BUILD_NUMBER']

###
### Logging
###
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)-8s %(message)s'
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)-8s %(name)s:%(lineno)s '
                       '%(message)s')
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_false'],
        },
        'stream': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {
            'handlers': ['stream'],
            'level': 'INFO',
        },
    },
}

if 'LOG_FILE' in os.environ:
    # add file handler and use in the app's logger
    LOGGING['handlers']['file'] = {
        'level': 'INFO',
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'formatter': 'verbose',
        'filename': os.environ['LOG_FILE'],
        'when': 'midnight',
        'backupCount': 7,
        'delay': True,
    }
    LOGGING['loggers']['apps']['handlers'] += ['file']


###
### Sentry
###
if 'SENTRY_RAVEN_DSN' in os.environ:
    RAVEN_CONFIG = {
        'dsn': os.environ['SENTRY_RAVEN_DSN'],
    }

    INSTALLED_APPS = INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',
    )


###
### Google Analytics
###
if 'GOOGLE_ANALYTICS_KEY' in os.environ and \
   'GOOGLE_ANALYTICS_DOMAIN' in os.environ:

    GOOGLE_ANALYTICS_KEY = os.environ['GOOGLE_ANALYTICS_KEY']
    GOOGLE_ANALYTICS_DOMAIN = os.environ['GOOGLE_ANALYTICS_DOMAIN']

    TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
        'utils.context_processors.google_analytics',
    )


###
### Bugherd
###
if 'BUGHERD_KEY' in os.environ:

    BUGHERD_KEY = os.environ['BUGHERD_KEY']

    TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
        'utils.context_processors.bugherd',
    )
