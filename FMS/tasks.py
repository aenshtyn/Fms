from celery import shared_task
from django.utils import timezone
from users.models import Farm
from services.whatsapp_service import WhatsAppService

@shared_task
def send_daily_metrics():
    now = timezone.now()
    farms = Farm.objects.all()
    whatsapp_service = WhatsAppService()

    for farm in farms:
        shareholders = farm.shareholders.all()
        message = f"Daily metrics for {farm.name}:\n"
        message += "Crops: 200 units harvested\n"
        message += "Milk: 500 liters produced\n"

        for shareholder in shareholders:
            if shareholder.phone_number:
                whatsapp_service.send_message(shareholder.phone_number, message)
