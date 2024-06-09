from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from typing import Optional
from src.products.Services.ProductService import ProductService


class CreateProduct(APIView):
    product_service: Optional[ProductService] = None

    def __init__(self, product_service):
        self.product_service = product_service

    def post(self, request, *args, **kwargs):
        try:
            product = self.product_service.createProductService(
                request_data=request.data
            )
            return Response({"product": product}, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response(
                e.args,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)


class GetAllProducts(APIView):
    product_service: Optional[ProductService] = None

    def __init__(self, product_service):
        self.product_service = product_service

    def get(self, request, *args, **kwargs):
        try:
            products = self.product_service.getAllProductsService()
            print(products)
            return Response({"products": products}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)


class UpdateProduct(APIView):
    product_service: Optional[ProductService] = None

    def __init__(self, product_service):
        self.product_service = product_service

    def post(self, request, id: UUID):
        try:
            self.product_service.updateProductService(product_id=id, data=request.data)
            return Response(status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, ValidationError) as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)


class GetProduct(APIView):
    product_service: Optional[ProductService] = None

    def __init__(self, product_service):
        self.product_service = product_service

    def get(self, request, id: UUID):
        try:
            product = self.product_service.getProductService(product_id=id)
            return Response(product)
        except (ObjectDoesNotExist, ValidationError) as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(APIView):
    product_service: Optional[ProductService] = None

    def __init__(self, product_service):
        self.product_service = product_service

    def delete(self, request, id: UUID):
        try:
            deleted = self.product_service.deleteProductService(product_id=id)
            if deleted:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
