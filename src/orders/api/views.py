from typing import Optional
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.orders.Services.OrderService import OrderService


class CreateOrder(APIView):
    order_service: Optional[OrderService] = None

    def __init__(self, order_service):
        self.order_service = order_service

    def post(self, request, *args, **kwargs):
        request_data = request.data
        data = self.order_service.createOrder(order_data=request_data)
        return Response(data, status=status.HTTP_201_CREATED)


class UpdateOrder(APIView):
    order_service: Optional[OrderService] = None

    def __init__(self, order_service):
        self.order_service = order_service

    def post(self, request, id, *args, **kwargs):
        request_data = request.data
        data = self.order_service.update_order(id, request_data)
        return Response(data, status=status.HTTP_200_OK)


class GetAllCurrentOrders(APIView):
    order_service: Optional[OrderService] = None

    def __init__(self, order_service):
        self.order_service = order_service

    def get(self, request, *args, **kwargs):
        response_data = self.order_service.getAllCurrentOrders()
        return Response(response_data, status=status.HTTP_200_OK)


class GetAllOrders(APIView):
    order_service: Optional[OrderService] = None

    def __init__(self, order_service):
        self.order_service = order_service

    def get(self, request, *args, **kwargs):
        response_data = self.order_service.getAllOrders()
        return Response(response_data, status=status.HTTP_200_OK)


class DeleteOrder(APIView):
    order_service: Optional[OrderService] = None

    def __init__(self, order_service):
        self.order_service = order_service

    def post(self, request, id):
        try:
            response = self.order_service.deleteOrder(order_id=id)

            if response:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status == status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)
