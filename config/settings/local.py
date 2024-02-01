from .base import *
DEBUG = bool(secrets.get('DEBUG',False))
#mongodb env variables
MONGO_DB = os.environ.get('MONGO_DB')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST')
MONGO_DB_PORT = os.environ.get('MONGO_DB_PORT')
MONGO_DB_CONNECTION_URL = os.environ.get('MONGO_DB_CONNECTION_URL')

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
