from django.contrib import admin
from .models import Order
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["id","User"]

    fields = ["id", "Products", "Address","User"]