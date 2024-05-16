# crops/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Crop
from inventory.models import Stock, Transaction

@receiver(post_save, sender=Crop)
def update_inventory_on_crop_production(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        stock, created = Stock.objects.get_or_create(product=product)
        stock.quantity += instance.quantity
        stock.save()

        # Record the transaction
        Transaction.objects.create(
            product=product,
            transaction_type='IN',
            quantity=instance.quantity,
            notes=f"Crop production ({instance.use}) of {instance.crop_type} on {instance.production_date}"
        )
