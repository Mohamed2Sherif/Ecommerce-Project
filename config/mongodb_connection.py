from django.conf import settings
from mongoengine import connect


url = settings.MONGO_DB_CONNECTION_URL
connect(HOST=url,db="OLA_Store")