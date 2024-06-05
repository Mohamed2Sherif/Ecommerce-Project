from django.db import models
from src.products.models import Product
from src.address.models import Address
from src.users.userprofiles import Customer


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
    size = models.CharField(max_length=50, null=True, blank=True, default="N/A")
    material = models.CharField(max_length=50, default="N/A")
    color = models.CharField(max_length=50, default="N/A")
    ship_date = models.DateField()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        db_table = "orders"
