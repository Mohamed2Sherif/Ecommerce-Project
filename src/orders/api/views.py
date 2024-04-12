from adrf.views import APIView
from rest_framework.permissions import IsAuthenticated
from src.orders.Services.contracts.IOrderService import IOrderService


class ListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    _orderService: IOrderService = None  # type: ignore

    def __init__(self, _orderService: IOrderService):  # type: ignore
        self._orderService = _orderService

    async def post(self, request, *args, **kwargs):
        user_data = request.user
        print(user_data.id)
        order_resposne = await self._orderService.createOrder(
            user=user_data, order_data=request.data
        )
        return order_resposne
