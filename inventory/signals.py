from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from .models import Stock

@receiver(post_save, sender=Stock)
def check_stock_level(sender, instance, **kwargs):
    if instance.check_stock_level():
        trigger_alert(instance)

def trigger_alert(stock_instance):
    # Define the alert mechanism here (e.g., send an email, log a message, etc.)
    print(f"Alert: The stock level of {stock_instance.product.name} is below the minimum required level!")
    # You can replace the print statement with your actual alert mechanism