from typing import Dict, List, Optional
from uuid import UUID
from asgiref.sync import sync_to_async
from celery import shared_task
from src.products.api.serializers import ProductSerializer
from src.products.models import Product
from src.products.Services.contracts.IPRepository import IProductRepository
from django.core.exceptions import ObjectDoesNotExist


class ProductRepository(IProductRepository):

    async def get_object_by_id(self, product_id: UUID) -> Product:
        try:
            product = await Product.objects.aget(id=product_id)
            return product
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(e.args)

    async def delete_product(self, product_id: UUID):
        try:
            numberOfObjectsDeleted = await Product.objects.filter(
                id=product_id
            ).adelete()
            return numberOfObjectsDeleted
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(e.args)

    @sync_to_async
    def get_all_products(self):
        return Product.objects.all()
