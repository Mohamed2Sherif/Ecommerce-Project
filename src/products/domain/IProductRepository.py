from abc import ABC, abstractmethod
from typing import List, Optional
from src.products.models import Product

class IProductRepository(ABC):

    @abstractmethod
    def addProduct(self, product: Product) -> Product:
        return NotImplementedError("AddProduct method is not implemented")

    @abstractmethod
    def getProduct(self, product_id: int) -> Optional[Product]:
        return NotImplementedError()

    @abstractmethod
    def getAllProducts(self) -> List[Product]:
        return NotImplementedError()

    @abstractmethod
    def updateProduct(self, product_id: int) -> Optional[Product]:
        return NotImplementedError()

    @abstractmethod
    def deleteProduct(self, product_id: int) -> None:
        return NotImplementedError
