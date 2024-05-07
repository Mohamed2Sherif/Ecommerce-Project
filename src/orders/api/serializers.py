from adrf import serializers as async_serializers
from src.orders.models import Order


class OrderSerializer(async_serializers.ModelSerializer):
    def validate_Products(self, value):
        pass

    # TODO:Create validation here
    class Meta:
        model = Order
        fields = ["Products", "Address"]
        read_only_fields = ["User", "created_time", "updated_time", "id"]
