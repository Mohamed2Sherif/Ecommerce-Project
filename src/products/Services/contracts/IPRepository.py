from abc import abstractmethod, ABC
from typing import List, Dict
from uuid import UUID
from antidote import injectable, interface
from asgiref.sync import sync_to_async
from src.products.models import Product

@interface
@injectable(lifetime='scoped')
class IProductRepository():
    
    async def get_object_by_id(self, id: UUID) -> Product:
        pass
    async def delete_product(self, product_id: UUID) -> bool:
        pass
    @sync_to_async
    def get_all_products(self):
        pass