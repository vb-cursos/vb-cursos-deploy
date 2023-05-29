from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['vbcursos-deploy.onrender.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.parse('postgres://site_vbcursos_user:nKN8Ke9CbQMSQ4MjjtAfUamlr6XeMDiD@dpg-chptlsik728ivvpvdml0-a.ohio-postgres.render.com/site_vbcursos')
}

'''
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.getenv("CLOUDINARY_URL"),
}
'''

CSRF_TRUSTED_ORIGINS = ['https://vbcursos-deploy.onrender.com']

# HTTPS settings

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

