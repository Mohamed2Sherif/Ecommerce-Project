from src.orders.Services.contracts.IOrderService import IOrderService
from src.orders.api.serializers import OrderSerializer
from src.orders.models import Order
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache


class OrderService(IOrderService):
    def createOrder(self, order_data):
        try:
            serializer = OrderSerializer(data=order_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = serializer.data
                cache.set("order_{data.order_id}", data)
                return data
        except Exception as e:
            raise Exception(e.args)

    def getAllOrders(self):
        try:
            data = cache.get("all_orders")
            if data:
                return data
            queryset = Order.objects.all()
            serializer = OrderSerializer(queryset, many=True)
            data = serializer.data
            cache.set("all_orders", data)
            return data
        except Exception as e:
            raise Exception(e.args)

    def getAllCurrentOrders(self):
        try:
            data = cache.get("current_orders")
            if data:
                return data
            queryset = Order.objects.filter(delivered=False).all()
            serializer = OrderSerializer(queryset, many=True)
            data = serializer.data
            cache.set("current_orders", data)
            return data
        except Exception as e:
            raise Exception(e.args)

    def update_order(self, order_id, updated_data):
        order_instance = Order.objects.get(order_id=order_id)
        serializer = OrderSerializer(instance=order_instance, data=updated_data)
        serializer.save()
        data = serializer.data
        cached_order = cache.get("order_{order_id}")
        if cached_order:
            cache.delete("order_{order_id}")
            cache.set("order_{order_id}", data)
        return data

    def deleteOrder(self, order_id):
        try:
            cached_order = cache.get("order_{order_id}")
            if cached_order:
                cache.delete("order_{order_id}")
            Deleted = Order.objects.get(order_id=order_id)
            deleted_count, _ = Deleted.delete()
            if deleted_count > 0:
                return True
            else:
                return False
        except ObjectDoesNotExist:
            raise Exception("Object doesn't exist,can't be deleted")
