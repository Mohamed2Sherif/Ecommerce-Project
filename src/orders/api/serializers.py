from rest_framework import serializers
from src.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    def validate_Products(self, value):
        pass

    # TODO:Create validation here
    class Meta:
        model = Order
        fields = ["Products", "Address"]
        read_only_fields = ["User", "created_time", "updated_time", "id"]
