from src.address.models import Address
from django.conf import settings
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to="Customerimages/")
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
