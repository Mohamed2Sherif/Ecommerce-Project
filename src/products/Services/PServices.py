from typing import Dict, List
from uuid import UUID
from django.db import IntegrityError
from src.products.Services.contracts.IPRepository import IProductRepository
from src.products.Services.contracts.IPService import IProductService
from src.products.api.serializers import ProductSerializer
from src.products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from django.core.cache import cache
class ProductService(IProductService):

    def __init__(self, product_repository: IProductRepository = None):  # type: ignore
        self.repository = product_repository

    async def createProductService(self, request_data):
        serializer = ProductSerializer(data=request_data)
        try:
            if serializer.is_valid(raise_exception=True):
                await serializer.asave()  # type:ignore
                data = await serializer.adata
                await cache.aset(data['id'],data)
                return data # type:ignore
        except ValidationError:
            raise ValidationError(serializer.errors)
        except IntegrityError as e:
            raise ValueError(e.args)

    async def updateProductService(self, product_id: UUID, data):
        try:
            instance = await self.repository.get_object_by_id(product_id)
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(e.args)
        try:
            serializer = ProductSerializer(instance=instance, data=data)
            if serializer.is_valid(raise_exception=True):
                await serializer.asave()  # type:ignore
                updated_product = await serializer.adata # type:ignore
                await cache.aset(str(product_id),updated_product)
                return updated_product
        except ValidationError:
            raise ValidationError(serializer.errors)

    async def getProductService(self, product_id):
        try : 
            cached_product = await cache.aget(str(product_id))
            if cached_product is not None:
                return cached_product
            else:
                product = await self.repository.get_object_by_id(product_id)
                serializer = ProductSerializer(product)
                data = await serializer.adata
                await cache.aset(str(data['id']),data)
                return data  # type: ignore
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(e.args)
    async def deleteProductService(self, product_id):
        try:
            
            numberOfObjects = await self.repository.delete_product(product_id)
            cache.delete(str(product_id))
            return True
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist

    async def getAllProductsService(self):
        try:
            products = await cache.aget('products')
            if products is not None:
                return products
            queryset = await self.repository.get_all_products()
            serializer = ProductSerializer(queryset, many=True)
            data = await serializer.adata
            await cache.aset('products',data)
            return data  # type:ignore

        except BaseException as e:
            raise ValueError(e.args)
