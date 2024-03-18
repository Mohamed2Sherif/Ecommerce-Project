from django.db import models
from utils.models import BaseModel

class Product(BaseModel):
    id = models.BigAutoField(primary_key=True,db_index=True)
    product_info = models.JSONField(default=dict)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "products"
    def __str__(self):
        return self.product_info['name']