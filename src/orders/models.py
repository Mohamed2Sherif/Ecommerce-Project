from django.db import models
from src.products.models import Product
from src.address.models import Address
from src.users.userprofiles import Customer


class Order(models.Model):
    User = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Products = models.ManyToManyField(Product)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)
