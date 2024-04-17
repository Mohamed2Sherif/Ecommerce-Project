from django.urls import path, re_path
from src.products.api import views

urlpatterns = [
    path(
        "products/",
        views.ProductsList.as_view(),
        name="createandlist_products",
    ),
    path(
        "product/<uuid:id>/",
        views.UpdateDeleteProduct.as_view(),
        name="get_update_delete_product",
    ),
]
