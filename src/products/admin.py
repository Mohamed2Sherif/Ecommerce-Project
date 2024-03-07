from django.contrib import admin
from src.products.models import Product
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
                models.JSONField: {'widget': JSONEditorWidget},
    }
    