from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def __init__(self, orderService):  # type: ignore
        self._orderService = orderService

    async def post(self, request, *args, **kwargs):
        user_data = request.user
        print(user_data.id)
        order_resposne = await self._orderService.createOrder(
            user=request.user, order_data=request.data
        )
        return Response(order_resposne)
