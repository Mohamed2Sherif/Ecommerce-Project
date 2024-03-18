from abc import ABC,abstractmethod
from typing import Dict

from src.products.models import Product

class IProductService(ABC):
    @abstractmethod
    def createProductService(self,request_data) -> Dict:
         return NotImplementedError
    @abstractmethod
    def updateProductService(self,product_id,data) -> Dict:
        return NotImplementedError
    @abstractmethod
    def getProductService(self,product_id) -> Product:
        return NotImplementedError
    @abstractmethod
    def deleteProductService(self,product_id):
        return NotImplementedError
    @abstractmethod
    def getAllProductsService(self):
        return NotImplementedError