from celery import shared_task
from .models import Product

@shared_task
def create_product_async(name, product_info, price):
    Product.objects.create(name=name, product_info=product_info, price=price)

@shared_task
def update_product_async(product_id, name, product_info, price):
    product = Product.objects.get(pk=product_id)
    product.name = name
    product.product_info = product_info
    product.price = price
    product.save()

@shared_task
def delete_product_async(product_id):
    Product.objects.filter(pk=product_id).delete()