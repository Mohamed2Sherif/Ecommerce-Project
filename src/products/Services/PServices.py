from typing import Dict, List
from uuid import UUID
from django.db import IntegrityError
from src.products.Services.contracts.IPRepository import IProductRepository
from src.products.Services.contracts.IPService import IProductService
from src.products.api.serializers import ProductSerializer
from src.products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError


class ProductService(IProductService):

    def __init__(self, product_repository: IProductRepository = None):  # type: ignore
        self.repository = product_repository

    async def createProductService(self, request_data):
        serializer = ProductSerializer(data=request_data)
        try:
            if serializer.is_valid(raise_exception=True):
                await serializer.asave()  # type:ignore
                return await serializer.adata  # type:ignore
        except ValidationError:
            raise ValidationError(serializer.errors)
        except IntegrityError:
            raise ValueError("Error Inserting Product to the database")

    async def updateProductService(self, product_id: UUID, data):
        try:
            instance = await self.repository.get_object_by_id(product_id)
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(e.args)
        try:
            serializer = ProductSerializer(instance=instance, data=data)
            if serializer.is_valid(raise_exception=True):
                await serializer.asave()  # type:ignore
                return serializer.adata  # type:ignore
        except ValidationError:
            raise ValidationError(serializer.errors)

    async def getProductService(self, product_id) -> Product:
        product = await self.repository.get_object_by_id(product_id)
        serializer = ProductSerializer(product)
        return await serializer.adata  # type: ignore

    async def deleteProductService(self, product_id):
        try:
            numberOfObjects = await self.repository.delete_product(product_id)
            return True
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist

    async def getAllProductsService(self) -> List[Product]:
        try:
            queryset = await self.repository.get_all_products()
            serializer = ProductSerializer(queryset, many=True)
            return await serializer.adata  # type:ignore

        except BaseException:
            raise ValueError("Error while fetching all products")
