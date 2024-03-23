from uuid import UUID
from django.core.exceptions import ObjectDoesNotExist
from adrf.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from src.products.Services.contracts.IPService import IProductService


class ProductsList(APIView):
    product_service: IProductService = None  # type: ignore

    def __init__(self, product_service: IProductService):
        self.product_service = product_service

    async def get(self, request, *args, **kwargs):
        try:
            products = await self.product_service.getAllProductsService()
            return Response({"products": products}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)

    async def post(self, request, *args, **kwargs):
        try:
            product = await self.product_service.createProductService(
                request_data=request.data
            )
            return Response({"product": product}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response(
                "error happend while creating the product",
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValidationError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteProduct(APIView):
    productservice: productservice = None  # type:ignore

    def __init__(self, productservice: IProductService):
        self.productservice = productservice

    async def post(self, request, id: UUID):
        try:
            await self.productservice.updateProductService(
                product_id=id, data=request.data
            )
            return Response(status=status.HTTP_200_OK)
        except (ObjectDoesNotExist, ValidationError) as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)

    async def get(self, request, id: UUID):
        try:
            product = await self.productservice.getProductService(product_id=id)
            return Response(product)
        except (ObjectDoesNotExist, ValidationError) as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)

    async def delete(self, request, id: UUID):
        try:
            deleted = await self.productservice.deleteProductService(product_id=id)
            if deleted:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
