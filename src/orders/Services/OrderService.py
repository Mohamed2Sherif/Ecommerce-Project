from src.orders.Services.contracts.IOrderService import IOrderService
from src.orders.api.serializers import OrderSerializer
from src.orders.models import Order
from django.core.exceptions import ObjectDoesNotExist


class OrderService(IOrderService):
    def createOrder(self, order_data):
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            return data

    def getAllOrders(self):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        data = serializer.data
        return data

    def getAllCurrentOrders(self):
        queryset = Order.objects.filter(delivered=False)
        serializer = OrderSerializer(queryset, many=True)
        return serializer.data

    def update_order(self, order_id, updated_data):
        order_instance = Order.objects.get(order_id=order_id)
        serializer = OrderSerializer(instance=order_instance, data=updated_data)
        serializer.save()
        return serializer.data

    def deleteOrder(self, order_id):
        try:
            Deleted = Order.objects.get(order_id=order_id)

            deleted_count, _ = Deleted.delete()
            if deleted_count > 0:
                return True
            else:
                return False
        except ObjectDoesNotExist:
            raise Exception("Object doesn't exist,can't be deleted")
