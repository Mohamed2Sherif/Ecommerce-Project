from django.urls import path


from .api.views import ListCreateView


urlpatterns = [
    
    path('create',ListCreateView.as_view(),name="ListCreateOrders")
]