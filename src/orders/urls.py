from django.urls import path


from src.orders.api.views import CreateOrderService


urlpatterns = [path("createOrder", CreateOrderService.as_view(), name="CreateOrders")]
