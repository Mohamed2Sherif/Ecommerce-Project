from rest_framework import serializers
from src.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = [
            "products",
            "price",
            "size",
            "material",
            "customer",
            "created_time",
            "updated_time",
            "id",
        ]
