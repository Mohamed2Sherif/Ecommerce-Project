from django.db import models
from utils.models import BaseModel
import uuid
from src.orders.utils import SizeChoices


class Category(BaseModel):
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    category_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="CategoryImages/")
    active = models.BooleanField()


class Product(BaseModel):
    product_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, db_index=True, editable=False
    )
    product_title = models.CharField(max_length=500)
    product_description = models.TextField()
    quantity = models.IntegerField
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_weight = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    available_sizes = models.CharField(
        max_length=100,
        default=SizeChoices.SMALL[0],
    )
    material = models.CharField(max_length=50, default="N/A", null=True, blank=True)
    available_colors = models.CharField(max_length=100, default="N/A")
    product_instock = models.BooleanField(default=True)
    discount_available = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="ProductImages/")

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "products"

    def __str__(self):
        return self.product_title
