from django.urls import path

from src.orders.Services.OrderService import OrderService

from .api.views import ListCreateView


orderservice = OrderService()
urlpatterns = [
    
    path('create',ListCreateView.as_view(_orderService=orderservice),name="ListCreateOrders")
]