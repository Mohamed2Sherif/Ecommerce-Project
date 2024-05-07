from .IProductService import IProductService
from antidote import implements
from typing import Dict, Any, List
from rest_framework.exceptions import ValidationError
from src.products.api.serializers import ProductSerializer
from django.core.cache import cache
from django.db import IntegrityError


@implements(IProductService)
class ProductService:
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

    def updateProductService(self, product_id, data) -> Dict:
        return NotImplementedError

    def getProductService(self, product_id) -> Any:
        return NotImplementedError

    def deleteProductService(self, product_id):
        return NotImplementedError

    def getAllProductsService(self) -> List[Any]:
        return NotImplementedError
