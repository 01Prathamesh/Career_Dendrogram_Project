# settings.py

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key - set via environment variable or fallback to a default key (not for production).
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-#gsap6gj3oj*t4&%1q-s^wp8)g25cuv6j&gm@7060c8wso$y-m')

# Debug mode - set via environment variable (use False in production).
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# Allowed hosts - set via environment variable, e.g., '127.0.0.1,localhost'.
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'careers',
    'accounts',
]

# Middleware settings - essential middlewares for security and session management.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'career_dendrogram.urls'

# Template settings - define template directories dynamically.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'careers', 'templates', 'accounts')],
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

# WSGI application entry point
WSGI_APPLICATION = 'career_dendrogram.wsgi.application'

# Database configuration - default to SQLite, can be overridden via environment.
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DJANGO_DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DJANGO_DB_USER', ''),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', ''),
        'HOST': os.getenv('DJANGO_DB_HOST', ''),
        'PORT': os.getenv('DJANGO_DB_PORT', ''),
    }
}

# Password validation settings - essential for security.
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

# Localization and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Directories to look for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'accounts', 'static'),
    os.path.join(BASE_DIR, 'careers', 'static'),
]

# Where to collect static files during deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Login/Logout redirects
LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'  # Uncomment to use

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication backends (custom backends can be added here)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Allowed Hosts for production
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
