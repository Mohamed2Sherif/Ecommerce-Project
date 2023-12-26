from django.db import models
from mongodb_connection import db
# Create your models here.



products_collection = db['Product']
