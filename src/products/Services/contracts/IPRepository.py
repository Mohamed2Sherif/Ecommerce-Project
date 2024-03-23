from abc import abstractmethod, ABC
from typing import List, Dict
from uuid import UUID
from asgiref.sync import sync_to_async
from src.products.models import Product
from celery import shared_task


class IProductRepository(ABC):

    @abstractmethod
    async def get_object_by_id(self, id: UUID) -> Product:
        return NotImplementedError

    @abstractmethod
    async def delete_product(self, product_id: UUID) -> bool:
        return NotImplementedError

    @abstractmethod
    @sync_to_async
    def get_all_products(self):
        return NotImplementedError
