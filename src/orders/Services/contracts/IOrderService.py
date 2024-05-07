from antidote import interface


@interface
class IOrderService:
    async def createOrder(self, user, order_data):
        raise NotImplementedError("you should implement createOrder Method")

    async def getOrder(self, order_id):
        raise NotImplementedError("you should implement getOrder Method")

    async def deleteOrder(self, order_id):
        raise NotImplementedError("you should implement deleteOrder Method")

    async def updateOrder(self, order, order_id):
        raise NotImplementedError("you should implement updateOrder Method")
