from django.conf import settings
from mongoengine import connect
name = settings.MONGO_DB_NAME
host = settings.MONGO_DB_HOST
port = settings.MONGO_DB_PORT
url = settings.MONGO_DB_CONNECTION_URL
connect(HOST=url,db="OLA_Store")