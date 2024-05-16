from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Production
from inventory.models import Stock, Transaction

@receiver(post_save, sender=Production)
def update_inventory_on_production(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        stock, created = Stock.objects.get_or_create(product=product)
        total_volume = instance.morning_volume + instance.evening_volume
        stock.quantity += total_volume
        stock.save()

        # Record the transaction
        Transaction.objects.create(
            product=product,
            transaction_type='IN',
            quantity=total_volume,
            notes=f"Milk production from {instance.cow} on {instance.milking_date}"
        )