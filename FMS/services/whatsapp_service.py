from twilio.rest import Client
from django.conf import settings

class WhatsAppService:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_message(self, to, message):
        from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
        to_whatsapp_number = f'whatsapp:{to}'
        self.client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)
