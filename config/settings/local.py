from .base import *
#mongodb env variables
MONGO_DB = get_env_variable('MONGO_DB')
MONGO_DB_NAME = get_env_variable('MONGO_DB_NAME')
MONGO_DB_HOST = get_env_variable('MONGO_DB_HOST')
MONGO_DB_PORT = get_env_variable('MONGO_DB_PORT')
MONGO_DB_CONNECTION_URL = get_env_variable('MONGO_DB_CONNECTION_URL')

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
