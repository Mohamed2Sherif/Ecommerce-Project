from django.urls import path
from src.products.api import views
from src.products.Services.PRepository import ProductRepository
from src.products.Services.PServices import ProductService  

product_service = ProductService(ProductRepository())

urlpatterns= [
    path('products/', views.ProductsList.as_view(productService=product_service), name='list_products'),
]