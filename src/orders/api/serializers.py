from adrf import serializers as async_serializers
from  rest_framework import serializers
from asgiref.sync import sync_to_async
from src.orders.models import Order
class OrderSerializer(async_serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ["Products","Address"]
        read_only_fields = ["User","created_time","updated_time","id"]