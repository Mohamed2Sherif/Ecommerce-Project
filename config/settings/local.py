from .base import *
DEBUG = bool(secrets.get('DEBUG',False))
#mongodb env variables
MONGO_DB = os.environ.get('MONGO_DB')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST')
MONGO_DB_PORT = os.environ.get('MONGO_DB_PORT')
MONGO_DB_CONNECTION_URL = os.environ.get('MONGO_DB_CONNECTION_URL')

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": BASE_DIR / "sqlite3.db"
    # }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
