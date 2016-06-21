from .base import *  # NOQA
import dj_database_url

DEBUG = (ENV_SETTING('DEBUG', 'true') == 'true')
COMPRESS_ENABLED = (ENV_SETTING('COMPRESS_ENABLED', 'true') == 'true')

try:
    from project.settings.local import DB_NAME, DB_USERNAME, DB_PASSWORD

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,                      # Or path to database file if using sqlite3.
            'USER': DB_USERNAME,                      # Not used with sqlite3.
            'PASSWORD': DB_PASSWORD,                  # Not used with sqlite3.
            'HOST': '/tmp/',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
except:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='sqlite:////' + ROOT_DIR + '/dev.db')}

EMAIL_BACKEND = ENV_SETTING('EMAIL_BACKEND',
                            'django.core.mail.backends.console.EmailBackend')

# Disable caching while in development
CACHES = {
    'default': {
        'BACKEND': ENV_SETTING('CACHE_BACKEND',
                               'django.core.cache.backends.dummy.DummyCache')
    }
}

# Add SQL statement logging in development
if (ENV_SETTING('SQL_DEBUG', 'false') == 'true'):
    LOGGING['loggers']['django.db'] = {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': False
    }

# set up Django Debug Toolbar if installed
try:
    import debug_toolbar  # noqa
    # MIDDLEWARE_CLASSES += (
    #     'debug_toolbar.middleware.DebugToolbarMiddleware',
    # )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    # DEBUG_TOOLBAR_CONFIG = {
    #     'SHOW_TOOLBAR_CALLBACK': "%s.true" % __name__,
    # }
    # DISABLE_PANELS = None
except ImportError:
    pass


# def true(request):
#     return True


# Set up django-extensions if installed
try:
    import django_extensions  # noqa
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass


# Enable django-compressor if it's installed
if COMPRESS_ENABLED:
    try:
        import compressor  # noqa
        INSTALLED_APPS += ('compressor',)
        STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)
    except ImportError:
        pass
