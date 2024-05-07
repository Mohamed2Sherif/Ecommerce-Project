from src.orders.Services.contracts.IOrderService import IOrderService
from src.orders.api.serializers import OrderSerializer
from rest_framework.serializers import ValidationError
from antidote import implements, injectable


@implements(IOrderService)
@injectable
class OrderService(IOrderService):
    async def createOrder(self, user, order_data):
        serializer = OrderSerializer(data=order_data)
        try:
            if serializer.is_valid(raise_exception=True):
                await serializer.asave(User=user)
                data = await serializer.adata
                return data
        except ValidationError:
            raise ValidationError(serializer.errors)

    async def getOrder(self, order_id):
        return "you should implement getOrder Method"

    async def deleteOrder(self, order_id):
        return "you should implement deleteOrder Method"

    async def updateOrder(self, order, order_id):
        return "you should implement updateOrder Method"
