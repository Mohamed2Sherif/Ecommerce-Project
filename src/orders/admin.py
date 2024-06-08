from django.contrib import admin
from .models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["order_id", "customer"]
    fields = ["order_id", "products", "order_address", "customer"]
