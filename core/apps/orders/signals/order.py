from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.orders.models import Order, OrderItem


@receiver(post_save, sender=Order)
def set_order_number(sender, instance, created, **kwargs):
    if created:
        last_order = Order.objects.order_by('order_number').last()
        instance.order_number = (last_order.order_number + 1) if last_order else 1
        instance.save(update_fields=["order_number"])