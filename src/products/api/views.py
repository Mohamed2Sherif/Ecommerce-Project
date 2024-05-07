from uuid import UUID
from antidote import inject,InjectMe
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from src.products.Services.contracts.IPService import IProductService


class ProductsList(APIView):

    @inject
    def __init__(self, product_service: InjectMe[IProductService] ):
        self.product_service = product_service

    def get(self, request, *args, **kwargs):
        try:
            products =  self.product_service.getAllProductsService()
            return Response({"products": products}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)

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


class UpdateDeleteProduct(APIView):


    @inject
    def __init__(self, productservice: InjectMe[IProductService]):
        self.productservice = productservice

    
    def post(self, request, id: UUID):
        try:
            self.productservice.updateProductService(
                product_id=id, data=request.data
            )
            return Response(status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, ValidationError) as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id: UUID):
        try:
            product = self.productservice.getProductService(product_id=id)
            return Response(product)
        except (ObjectDoesNotExist, ValidationError) as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: UUID):
        try:
            deleted = self.productservice.deleteProductService(product_id=id)
            if deleted:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
