from django.urls import path
from src.products.api import views
from src.products.Services.ProductService import ProductService

urlpatterns = [
    path(
        "CreateProduct/",
        views.CreateProduct.as_view(product_service=ProductService()),
        name="createandlist_products",
    ),
    path(
        "product/<uuid:id>/",
        views.UpdateProduct.as_view(product_service=ProductService()),
        name="updateProduct",
    ),
    path(
        "product/<uuid:id>/",
        views.GetProduct.as_view(product_service=ProductService(), name="GetProduct"),
    ),
    path(
        "products/",
        views.GetAllProducts.as_view(product_service=ProductService()),
        name="GetAllProducts",
    ),
    path(
        "product/<uuid:id>/",
        views.DeleteProduct.as_view(product_service=ProductService()),
        name="DeleteProduct",
    ),
]
