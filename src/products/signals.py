from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product
from django.core.cache import cache


@receiver([post_save, post_delete], sender=Product)
def update_product_cache(sender, instance, **kwargs):
    # Invalidate product cache
    cache.delete("product_list")


# @receiver(post_save, sender=Product)
# def create_product_signal(sender, instance, created, **kwargs):
#     if created:
#         create_product_task.delay(instance.name, instance.product_info, instance.price)

# @receiver(post_save, sender=Product)
# def update_product_signal(sender, instance, created, **kwargs):
#     if not created:
#         update_product_task.delay(instance.id, instance.name, instance.product_info, instance.price)

# @receiver(post_delete, sender=Product)
# def delete_product_signal(sender, instance, **kwargs):
#     delete_product_task.delay(instance.id)
