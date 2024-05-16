from celery import shared_task
from FMS.services.whatsapp_service import WhatsAppService




@shared_task
def send_daily_metrics(phone_number):
    from django.utils import timezone
    from django.db.models import Sum, Count
    from dairy.models import Production

    today = timezone.now().date()

    # Calculate today's total milk production
    today_milk_production = Production.day_total_volume(today)[2]

    # Calculate yesterday's total milk production
    yesterday_milk_production = Production.day_total_volume(today - timezone.timedelta(days=1))[2]

    # Calculate the change in milk production
    milk_change = today_milk_production - yesterday_milk_production

    message = (
        f"Daily Farm Analytics:\n\n"
        f"Milk Production Today: {today_milk_production} liters\n"
        f"Change in Milk Production: {milk_change} liters\n"
    )
    
    # Send the WhatsApp message
    whatsapp_service = WhatsAppService()
    whatsapp_service.send_message(phone_number, message)



@shared_task
def send_whatsapp_message(phone_number, message):
    whatsapp_service = WhatsAppService()
    whatsapp_service.send_message(phone_number, message)
