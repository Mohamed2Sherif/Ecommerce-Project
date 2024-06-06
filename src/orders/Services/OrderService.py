from src.orders.Services.contracts.IOrderService import IOrderService
from src.orders.api.serializers import OrderSerializer


class OrderService(IOrderService):
    def createOrder(self, order_data):
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save
            data = serializer.data
            return data

    def getAllOrders(self):
        pass

    def getAllCurrentOrders(self):
        pass

    def update_order(self, order_id, updated_data):
        pass

    def deleteOrder(self, order_id):
        pass
