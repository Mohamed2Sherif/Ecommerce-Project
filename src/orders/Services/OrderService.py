from src.orders.Services.contracts.IOrderService import IOrderService
from src.orders.api.serializers import OrderSerializer

from rest_framework.serializers import ValidationError
class OrderService(IOrderService):
        
    async def createOrder(self,order_data):
        serializer = OrderSerializer(data=order_data)
        try:
            if serializer.is_valid(raise_exception=True):
                await serializer.asave() # type: ignore
                data = await serializer.adata # type: ignore
                return data
        except ValidationError as e:
            raise ValidationError(serializer.errors)
        
    async def getOrder(self, order_id):
        return ("you should implement getOrder Method")

    async def deleteOrder(self, order_id):
        return("you should implement deleteOrder Method")

    async def updateOrder(self, order, order_id):
       return("you should implement updateOrder Method")
