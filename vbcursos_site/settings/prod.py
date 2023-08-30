from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['vbcursos-deploy.onrender.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("PGDATABASE"),
        'USER': os.getenv("PGUSER"),
        'PASSWORD': os.getenv("PGPASSWORD"),
        'HOST': os.getenv("PGHOST"),
        'PORT': os.getenv("PGPORT"),
    }
}

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.getenv("CLOUDINARY_URL"),
}

CSRF_TRUSTED_ORIGINS = ['https://vbcursos-deploy.onrender.com']

# HTTPS settings

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

