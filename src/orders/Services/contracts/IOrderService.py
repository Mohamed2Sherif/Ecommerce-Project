from abc import ABC, abstractmethod


class IOrderService(ABC):
    @abstractmethod
    async def createOrder(self, user, order_data):
        raise NotImplementedError("you should implement createOrder Method")

    @abstractmethod
    async def getOrder(self, order_id):
        raise NotImplementedError("you should implement getOrder Method")

    @abstractmethod
    async def deleteOrder(self, order_id):
        raise NotImplementedError("you should implement deleteOrder Method")

    @abstractmethod
    async def updateOrder(self, order, order_id):
        raise NotImplementedError("you should implement updateOrder Method")
