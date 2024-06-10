from django.urls import path
from src.orders.Services.OrderService import OrderService


from src.orders.api.views import (
    CreateOrder,
    GetAllCurrentOrders,
    GetAllOrders,
    UpdateOrder,
    DeleteOrder,
)


urlpatterns = [
    path(
        "createOrder",
        CreateOrder.as_view(order_service=OrderService()),
        name="CreateOrders",
    ),
    path(
        "updateOrder/{int:id}",
        UpdateOrder.as_view(order_service=OrderService()),
        name="updateOrder",
    ),
    path(
        "deleteOrder/{int:id}",
        DeleteOrder.as_view(order_service=OrderService()),
        name="deleteOrder",
    ),
    path(
        "getAllOrders",
        GetAllOrders.as_view(order_service=OrderService()),
        name="allOrders",
    ),
    path(
        "getAllCurrentOrders",
        GetAllCurrentOrders.as_view(order_service=OrderService()),
        name="currentOrders",
    ),
]
