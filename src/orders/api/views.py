from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.orders.Services.OrderService import OrderService


class CreateOrderService(APIView):
    order_service = OrderService()

    def post(self, request, *args, **kwargs):
        request_data = request.data
        data = self.order_service.createOrder(order_data=request_data)
        return Response(data, status=status.HTTP_201_CREATED)
