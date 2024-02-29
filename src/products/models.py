from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_info = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name