from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product
from django.core.cache import cache


@receiver(post_save, sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    cache.delete(f'product_{instance.id}')
    cache.delete_pattern('product_list_*')