from typing import List, Optional
from src.products.api.serializers import ProductSerializer
from src.products.models import Product
from src.products.Services.contracts.IPRepository import IProductRepository
from django.core.exceptions import ObjectDoesNotExist


class ProductRepository(IProductRepository):
    
    
    def create_product(self, data):
        serializer = ProductSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def get_object_by_id(self, product_id: int):
        product = Product.objects.get(id=id)
        return product

    def update_product(self, instance, data):
        serializer = ProductSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def delete_product(self, product_id: int):
        try:
            Product.objects.filter(id=product_id).delete()
            return True
        except ObjectDoesNotExist:
            return False

    def get_all_products(self):
        return Product.objects.all()
