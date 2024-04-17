from adrf import serializers as async_serializers
from  rest_framework import serializers
from src.address.models import Address
from src.orders.models import Order
class OrderSerializer(async_serializers.ModelSerializer):
    def validate_Products(self, value):
        for product in value:
            
    class Meta:
        model = Order
        fields = ["Products","Address"]
        read_only_fields = ["User","created_time","updated_time","id"]