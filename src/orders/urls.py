from django.urls import path


from src.orders.api.views import (
    CreateOrder,
    GetAllCurrentOrders,
    GetAllOrders,
    UpdateOrder,
    DeleteOrder,
)


urlpatterns = [
    path("createOrder", CreateOrder.as_view(), name="CreateOrders"),
    path("updateOrder/{int:id}", UpdateOrder.as_view(), name="updateOrder"),
    path("deleteOrder/{int:id}", DeleteOrder.as_view(), name="deleteOrder"),
    path("getAllOrders", GetAllOrders.as_view(), name="allOrders"),
    path("getAllCurrentOrders", GetAllCurrentOrders.as_view(), name="currentOrders"),
]
