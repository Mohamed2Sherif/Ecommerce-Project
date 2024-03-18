from django.urls import path
from .api.views import *

urlpatterns =[
    path('products/', list_products, name='list_products'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]