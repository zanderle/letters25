"""
Django settings for letters25 project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#)nz_y%)s2e2st2s^m%8l*54iyr*(8^n=i*#lbirp79d2ule^x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'filer',
    'mptt',
    'easy_thumbnails',
    'letters_collection',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'letters25.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'letters25.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'letters',
        'USER': 'letters',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))


STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, '..', 'letters_collection', 'static', 'bower_components'),
)

PIPELINE_CSS = {
    'pace': {
        'source_filenames': (
            'pace/themes/red/pace-theme-minimal.css',
        ),
        'output_filename': 'css/pace-theme.min.css',
    },
    'font-awesome': {
        'source_filenames': (
            'font-awesome/less/font-awesome.less',
        ),
        'output_filename': 'css/font-awesome.min.css'
    },
    # Custom styling
    'custom': {
        'source_filenames': (
            'less/style.less',
        ),
        'output_filename': 'css/custom.min.css',
    }
}

PIPELINE_JS = {
    # Libraries
    'jquery': {
        'source_filenames': (
            'jquery/dist/jquery.js',
        ),
        'output_filename': 'js/jquery.js',
    },
    'vendor': {
        'source_filenames': (
            'bootstrap/dist/js/bootstrap.js',
        ),
        'output_filename': 'js/vendor.js',
    },
    'pace': {
        'source_filenames': (
            'pace/pace.js',
        ),
        'output_filename': 'js/pace.js',
    },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

# Retina support for easy_thumbnails
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_ALIASES = {
    '': {
        'list-size': {'size': (50, 50), 'crop': True},
        'featured': {'size': (800, 436.5), 'quality': 100}
    },
}

try:
    from .local_settings import *
except:
    pass
