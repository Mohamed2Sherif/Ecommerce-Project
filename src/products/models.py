from django.db import models

class Product(models.Model):
    product_info = models.JSONField(default=dict)
    def __str__(self):
        return self.product_info['name']