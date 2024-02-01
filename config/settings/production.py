from .base import *
DEBUG = bool(secrets.get('DEBUG'))
ALLOWED_HOSTS = []

MONGO_DB = os.environ.get('MONGO_DB')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')
MONGO_DB_HOST = os.environ.get('MONGO_DB_HOST')
MONGO_DB_PORT = os.environ.get('MONGO_DB_PORT')
MONGO_DB_CONNECTION_URL = os.environ.get('MONGO_DB_CONNECTION_URL')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": secrets.get('POSTGRESDB_NAME'),
        "USER":secrets.get('POSTGRESDB_USER'),
        "PASSWORD": secrets.get('POSTGRESDB_PASSWORD'),
        "HOST": secrets.get('POSTGRESDB_HOST'),
        "port":secrets.get('POSTGRESDB_PORT'),
    }

}