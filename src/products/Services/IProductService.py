from abc import ABC, abstractmethod
from typing import Dict, List, Any

from antidote import interface

from src.products.models import Product


@interface
class IProductService(ABC):
    @abstractmethod
    def createProductService(self, request_data) -> Any:
        return NotImplementedError

    @abstractmethod
    def updateProductService(self, product_id, data) -> Dict:
        return NotImplementedError

    @abstractmethod
    def getProductService(self, product_id) -> Product:
        return NotImplementedError

    @abstractmethod
    def deleteProductService(self, product_id):
        return NotImplementedError

    @abstractmethod
    def getAllProductsService(self) -> List[Product]:
        return NotImplementedError
