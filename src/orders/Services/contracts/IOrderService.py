from abc import ABC, abstractmethod


class IOrderService(ABC):
    @abstractmethod
    def createOrder(self, order_data):
        raise NotImplementedError

    @abstractmethod
    def getAllOrders(self):
        raise NotImplementedError

    @abstractmethod
    def getAllCurrentOrders(self):
        raise NotImplementedError

    @abstractmethod
    def update_order(self, order_id, updated_data):
        raise NotImplementedError

    @abstractmethod
    def deleteOrder(self, order_id):
        raise NotImplementedError
