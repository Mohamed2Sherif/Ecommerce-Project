from django.db import models
from src.products.models import Product
from src.address.models import Address
from src.users.userprofiles import Customer
from .utils import SizeChoices


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.CharField(
        max_length=20, choices=[("on_delivery", "On Delivery"), ("online", "Online")]
    )
    order_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    ship_date = models.DateField()
    delivered = models.BooleanField(default=False, db_index=True)
    size = models.CharField(
        max_length=10,
        choices=SizeChoices.CHOICES,
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = "orders"
