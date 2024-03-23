from abc import ABC, abstractmethod
from typing import Dict, List

from src.products.models import Product


class IProductService(ABC):
    @abstractmethod
    async def createProductService(self, request_data) -> Dict:
        return NotImplementedError

    @abstractmethod
    async def updateProductService(self, product_id, data) -> Dict:
        return NotImplementedError

    @abstractmethod
    async def getProductService(self, product_id) -> Product:
        return NotImplementedError

    @abstractmethod
    async def deleteProductService(self, product_id):
        return NotImplementedError

    @abstractmethod
    async def getAllProductsService(self) -> List[Product]:
        return NotImplementedError
