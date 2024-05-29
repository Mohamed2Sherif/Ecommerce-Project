from src.products.models import Product
from .IProductService import IProductService
from typing import Any
from rest_framework.exceptions import ValidationError
from src.products.api.serializers import ProductSerializer
from django.core.cache import cache
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class ProductService(IProductService):
    def createProductService(self, request_data) -> Any:
        try:
            serializer = ProductSerializer(data=request_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = serializer.data
                cache.set(data["id"], data)
                return data
        except ValidationError:
            raise ValidationError(serializer.errors)
        except IntegrityError as e:
            raise ValueError(e.args)

    def updateProductService(self, product_id, data) -> Any:
        try:
            instance = Product.objects.get(product_id)
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(e.args)
        try:
            serializer = ProductSerializer(instance=instance, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                updated_product = serializer.data
                cache.set(str(product_id), updated_product)
                return updated_product
        except ValidationError:
            raise ValidationError(serializer.errors)

    def getProductService(self, product_id) -> Any:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        data = serializer.data
        return data

    def deleteProductService(self, product_id) -> Any:
        try:
            if Product.objects.get(id=product_id).delete():
                cache.delete(str(product_id))
            return True
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist

    def getAllProductsService(self) -> Any:
        cached_data = cache.get("products")
        if cached_data:
            return cached_data
        else:
            try:
                rows = Product.objects.all()
                serializer = ProductSerializer(rows, many=True)
                data = serializer.data
                cache.set("products", data)
                return data

            except Exception as e:
                raise ValueError(e.args)
