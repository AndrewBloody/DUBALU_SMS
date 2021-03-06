"""
Django settings for dubalu project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import warnings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')!)e(o7q!$78ili$vnj=q4cokf1u#!p92%!=v2#)$yv81w+nmz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEST = 'test' in sys.argv

################################################################################
#      ____            _           _
#     |  _ \ _ __ ___ (_) ___  ___| |_
#     | |_) | '__/ _ \| |/ _ \/ __| __|
#     |  __/| | | (_) | |  __/ (__| |_
#     |_|   |_|  \___// |\___|\___|\__|
#                   |__/
# PROJECT variables:

PROJECT_TITLE = 'Dubalu Framework'
COPYRIGHT = '2014, deipi.com LLC'
VERSION = '2.0'
RELEASE = '2.0'

PROJECT_NAME, __, PROJECT_SUFFIX = os.getenv('PROJECT', '').partition('.')
if not PROJECT_NAME:
    PROJECT_NAME = os.getenv('PROJECT_NAME', '')
    if not PROJECT_NAME:
        try:
            PROJECT_FILE = os.path.join(BASE_DIR, 'PROJECT')
            PROJECT_NAME, __, PROJECT_SUFFIX = open(PROJECT_FILE, 'rt').read().strip().partition('.')
        except IOError:
            warnings.warn("No PROJECT_NAME assigned (missing '%s'?)")
            sys.exit(1)
PROJECT_NAME = PROJECT_NAME.replace('-', '_')

if not PROJECT_SUFFIX:
    PROJECT_SUFFIX = os.getenv('PROJECT_SUFFIX', '')
    if not PROJECT_SUFFIX:
        try:
            PROJECT_SUFFIX = open(os.path.join(BASE_DIR, 'PROJECT_SUFFIX'), 'rt').read().strip()
        except IOError:
            PROJECT_SUFFIX = ''

if PROJECT_NAME == 'default':
    PROJECT_NAME = None
    PROJECT_SUFFIX = None

SETTINGS = {}

HANDLER400 = 'dfw.views.bad_request'
HANDLER403 = 'dfw.views.permission_denied'
HANDLER404 = 'dfw.views.page_not_found'
HANDLER500 = 'dfw.views.server_error'

################################################################################
#      ___           _        _ _          _      _
#     |_ _|_ __  ___| |_ __ _| | | ___  __| |    / \   _ __  _ __  ___
#      | || '_ \/ __| __/ _` | | |/ _ \/ _` |   / _ \ | '_ \| '_ \/ __|
#      | || | | \__ \ || (_| | | |  __/ (_| |  / ___ \| |_) | |_) \__ \
#     |___|_| |_|___/\__\__,_|_|_|\___|\__,_| /_/   \_\ .__/| .__/|___/
#                                                     |_|   |_|
# Application definition


INSTALLED_APPS = TESTS = ()

if not TEST and PROJECT_NAME:
    _INSTALLED_APPS = (
        PROJECT_NAME,
    )
    INSTALLED_APPS += _INSTALLED_APPS
    TESTS += _INSTALLED_APPS

_INSTALLED_APPS = (
    'dfw',
    'nestedforms',
)
INSTALLED_APPS += _INSTALLED_APPS
TESTS += _INSTALLED_APPS

INSTALLED_APPS += (
    # 'django.contrib.admin',  # Not used! Admin app not being enabled for dubalu
    # 'django.contrib.auth',  # Not used! Using dfw.users and dfw.registration instead.
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

_INSTALLED_APPS = (
    'dfw.core',
    'dfw.registration',
    'dfw.users',
    'dfw.entities',
    # 'dfw.permissions',
    # 'dfw.profiles',
    # 'dfw.relationships',
    'dfw.contrib.pages',
    'dfw.contrib.bundles',
)
INSTALLED_APPS += _INSTALLED_APPS
TESTS += _INSTALLED_APPS

_INSTALLED_APPS = (
    'common_views',
    'lazyforms',
    'uuidfield',  # Used for being able to have short encoded uuids
)
INSTALLED_APPS += _INSTALLED_APPS
TESTS += _INSTALLED_APPS

INSTALLED_APPS += (
    'crispy_forms',
    'crispy_extra_fields',
    'endless_pagination',
    # 'social.apps.django_app',
    'coffin',
    'storages',
)

INSTALLED_APPS += (
    'django_assets',
    'django_extensions',
)

INSTALLED_APPS += (
    'djcelery',

)

if TEST and PROJECT_NAME:
    # While in tests, give priority to dfw app and templates.
    INSTALLED_APPS += (PROJECT_NAME,)
    TESTS += (PROJECT_NAME,)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'dfw.entities.middleware.EntityMiddleware',
)

ROOT_URLCONF = 'dfw.urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
'''
# Variables for Database
DATABASE_NAME = os.getenv('DATABASE_NAME','dubalu_{PROJECT_NAME}.{PROJECT_SUFFIX}.db')
DATABASE_HOST = os.getenv('DATABASE_HOST', '172.16.100.201')
DATABASE_PORT = os.getenv('DATABASE_PORT', 5432)
PROJECT_USER = os.getenv('PROJECT_USER', 'dubalu')
'''

# Old DATABASE CONFIG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



'''# New DATABASE CONFIG 
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'dubalu_sms_v2',
    'USER': '{PROJECT_USER}',
    'HOST': '{DATABASE_HOST}',
    'PORT': '{DATABASE_PORT}',
    'CONN_MAX_AGE': None,
    }
}
'''
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


################################################################################
#      _____                    _       _
#     |_   _|__ _ __ ___  _ __ | | __ _| |_ ___  ___
#       | |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \/ __|
#       | |  __/ | | | | | |_) | | (_| | ||  __/\__ \
#       |_|\___|_| |_| |_| .__/|_|\__,_|\__\___||___/
#                        |_|
#
# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'dfw.core.context_processors.core',
    # 'dfw.sections.context_processors.base_template',
    'dfw.entities.context_processors.entity',
    # 'dfw.profiles.context_processors.profiles',

    # 'social.apps.django_app.context_processors.backends',
    # 'social.apps.django_app.context_processors.login_redirect',
    # 'pushstream.context_processors.pushstreams',
)
if PROJECT_NAME:
    TEMPLATE_CONTEXT_PROCESSORS += (
        PROJECT_NAME + '.context_processors.default',
    )
TEMPLATE_DEBUG = None

TEMPLATE_DIRS = (
    os.path.join('{BASE_DIR}', 'projects', '{PROJECT_NAME}', 'storage'),  # Needed by dfw.contrib.pages
)
if TEST:
    TEMPLATE_DIRS += (
        os.path.join('{BASE_DIR}', 'dfw', 'templates', 'tests'),  # Override templates for tests
    )

# List of callables that know how to import templates from various sources.
# See the comments in django/core/template/loader.py for interface
# documentation.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Use Jinja2 engine:
JINJA2_ENABLED = True
# JINJA2_USE_COMPILED = True
# JINJA2_COMPILED_TEMPLATES = os.path.join('{CACHE_ROOT}', '_jinja2') if JINJA2_USE_COMPILED else None


################################################################################
#         _                 _
#        / \   ___ ___  ___| |_ ___
#       / _ \ / __/ __|/ _ \ __/ __|
#      / ___ \\__ \__ \  __/ |_\__ \
#     /_/   \_\___/___/\___|\__|___/
#

DEFAULT_FILE_STORAGE = 'dfw.core.storage.QueuedFileSystemStorage'
STATICFILES_STORAGE = 'dfw.core.storage.StaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_assets.finders.AssetsFinder',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'projects', '{PROJECT_NAME}', 'www', 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'projects', '{PROJECT_NAME}', 'www', 'media')
STORAGE_ROOT = os.path.join(BASE_DIR, 'projects', '{PROJECT_NAME}', 'storage')
DATA_ROOT = os.path.join(BASE_DIR, 'projects', '{PROJECT_NAME}', 'data')


################################################################################
#       ____      _                   _____
#      / ___|_ __(_)___ _ __  _   _  |  ___|__  _ __ _ __ ___  ___
#     | |   | '__| / __| '_ \| | | | | |_ / _ \| '__| '_ ` _ \/ __|
#     | |___| |  | \__ \ |_) | |_| | |  _| (_) | |  | | | | | \__ \
#      \____|_|  |_|___/ .__/ \__, | |_|  \___/|_|  |_| |_| |_|___/
#                      |_|    |___/
#
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False


################################################################################
#       ____     _
#      / ___|___| | ___ _ __ _   _
#     | |   / _ \ |/ _ \ '__| | | |
#     | |__|  __/ |  __/ |  | |_| |
#      \____\___|_|\___|_|   \__, |
#                            |___/
#
os.environ.setdefault('CELERY_LOADER', 'djcelery.loaders.DjangoLoader')  # This is the equivalent of calling ``djcelery.setup_loader()``
# Celery Results Settings:
CELERY_IGNORE_RESULT = True
CELERY_RESULT_BACKEND = 'redis://127.0.0.1'
CELERY_TASK_RESULT_EXPIRES = 600
# Celery Broker Settings:
BROKER_URL = 'amqp://guest@127.0.0.1//'  # RabbitMQ Management at http://localhost:15672/
BROKER_TRANSPORT_OPTIONS = dict(
    keyprefix='{PROJECT_NAME}.{PROJECT_SUFFIX}',
)
# Celery Task Execution Settings:
CELERY_ALWAYS_EAGER = False
CELERY_SEND_EVENTS = False
CELERY_DISABLE_RATE_LIMITS = True
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'default'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'  # Celery Periodic Task Server (celerybeat)

# Queue configuration
from kombu import Queue
CELERY_QUEUES = (
    Queue('default', routing_key='default'),
)
CELERY_DEFAULT_QUEUE = 'default'


################################################################################
#     __        __   _                        _
#     \ \      / /__| |__   __ _ ___ ___  ___| |_ ___
#      \ \ /\ / / _ \ '_ \ / _` / __/ __|/ _ \ __/ __|
#       \ V  V /  __/ |_) | (_| \__ \__ \  __/ |_\__ \
#        \_/\_/ \___|_.__/ \__,_|___/___/\___|\__|___/
#
ASSETS_CACHE = True
ASSETS_DEBUG = False
ASSETS_AUTO_BUILD = True
ASSETS_UPDATER = 'timestamp'
ASSETS_VERSIONS = 'hash'
ASSETS_MANIFEST = 'cache'
ASSETS_URL_EXPIRE = True

UGLIFYJS_BIN = ['node', os.path.join(BASE_DIR, 'lib/js/compiler.js')]
UGLIFYJS_EXTRA_ARGS = ['--uglify', '--preprocess', '--unsafe']
UGLIFYJS_DISABLED = False

PYSCSS_STYLE = 'compressed'
PYSCSS_DEBUG_INFO = False
PYSCSS_LOAD_PATHS = [
    os.path.join(BASE_DIR, 'dubalu/dfw/contrib/bundles/static/src/css'),
    os.path.join(BASE_DIR, 'dubalu/dfw/contrib/bundles/static/src/sass/frameworks'),
]

AUTOPREFIXER_BIN = ['node', os.path.join(BASE_DIR, 'lib/js/autoprefixer.js')]
AUTOPREFIXER_BROWSERS = ['last 3 versions', 'bb 10', 'android 3', 'ie 7', 'ie 8']

################################################################################
#       ___  _   _                 ____       _   _   _
#      / _ \| |_| |__   ___ _ __  / ___|  ___| |_| |_(_)_ __   __ _ ___
#     | | | | __| '_ \ / _ \ '__| \___ \ / _ \ __| __| | '_ \ / _` / __|
#     | |_| | |_| | | |  __/ |     ___) |  __/ |_| |_| | | | | (_| \__ \
#      \___/ \__|_| |_|\___|_|    |____/ \___|\__|\__|_|_| |_|\__, |___/
#                                                             |___/
DEPENDENCIES = {}
globs = globals()

################################################################################
# Load settings for all apps (if available):
from dfw.utils.extendsettings import extend_settings
extend_settings(globs, exclude=('django_assets', 'endless_pagination', 'imagekit', 'django_extensions'), extra=(PROJECT_NAME, '%s.local' % PROJECT_NAME))

# Check dependencies:
for app, dependencies in DEPENDENCIES.items():
    previous_apps = INSTALLED_APPS[:INSTALLED_APPS.index(app) + 1]
    for dependency in dependencies:
        if dependency not in INSTALLED_APPS:
            sys.stderr.write("App '%s' depends on '%s'\n" % (app, dependency))
            sys.exit(1)
        if dependency not in previous_apps:
            warnings.warn("App '%s' should be listed before '%s' in INSTALLED_APPS." % (dependency, app))

################################################################################

if DEBUG is None:
    DEBUG = False


if TEMPLATE_DEBUG is None:
    TEMPLATE_DEBUG = False


# Jinja2 configuration:
JINJA2_TEMPLATE_LOADERS = TEMPLATE_LOADERS
if JINJA2_ENABLED:
    TEMPLATE_LOADERS = (
        'coffin.template.loaders.jinja2.Loader',
    )


# Setup debug level for logging
DEBUG_OR_WARNING = 'DEBUG' if DEBUG else 'WARNING'

################################################################################
# Interpolate `{VAR_NAME}`-like variables in strings in certain settings:
from recursiveformat import recursive_format
recursive_format(globs, **globs)


################################################################################
if PROJECT_SUFFIX:
    PROJECT = '%s.%s' % (PROJECT_NAME, PROJECT_SUFFIX)
else:
    PROJECT = PROJECT_NAME
