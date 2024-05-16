from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from .models import User, Farm, Invitation
from .serializers import UserSerializer, FarmSerializer, InvitationSerializer, FarmUsersSerializer
from .permissions import IsFarmOwner
from django.http import HttpResponse
from .tasks import send_whatsapp_message, send_daily_metrics

class InvitationViewSet(viewsets.ModelViewSet):
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        invitation = serializer.instance
        send_mail(
            'Farm Invitation',
            f'You have been invited to join the farm {invitation.farm.name} as a {invitation.role}. Please register using this link: http://localhost:4200/register/{invitation.token}',
            'from@example.com',
            [invitation.email],
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

    def get_permissions(self):
        if self.action in ['list_users']:
            self.permission_classes = [IsFarmOwner]
        return super().get_permissions()

    @action(detail=True, methods=['get'])
    def list_users(self, request, pk=None):
        farm = self.get_object()
        serializer = FarmUsersSerializer(farm)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework.views import APIView

class RegisterInvitedUser(APIView):
    def post(self, request, token):
        invitation = Invitation.objects.filter(token=token, accepted=False).first()
        if not invitation:
            return Response({'detail': 'Invalid or expired invitation token'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            if invitation.role == 'MANAGER':
                invitation.farm.managers.add(user)
            elif invitation.role == 'SHAREHOLDER':
                invitation.farm.shareholders.add(user)
            elif invitation.role == 'GUEST':
                invitation.farm.guests.add(user)
            invitation.accepted = True
            invitation.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def send_message_view(request):
    # phone_number = '+254714347036'
    phone_number = '+254720299258'
    message = 'Hello Evans, this is a sample Whatsapp Message from FarmSync! The System Being Developed by Super Engineer'
    send_whatsapp_message.delay(phone_number, message)
    return HttpResponse('WhatsApp message is being sent asynchronously')


def send_analytics_view(request):
    phone_number = '+254714347036'
    send_daily_metrics.delay(phone_number)
    return HttpResponse('Daily analytics WhatsApp message is being sent asynchronously.')