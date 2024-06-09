from django.contrib import admin
from src.products.models import Product
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["product_id"]

    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    fields = ["product_id", "product_info", "category_info"]
