from django.urls import path, re_path
from src.products.api import views
from src.products.Services.PRepository import ProductRepository
from src.products.Services.PServices import ProductService

product_service = ProductService(ProductRepository())

urlpatterns = [
    path(
        "products/",
        views.ProductsList.as_view(product_service=product_service),
        name="createandlist_products",
    ),
    path(
        "product/<uuid:id>/",
        views.UpdateDeleteProduct.as_view(productservice=product_service),
        name="get_update_delete_product",
    ),
]
