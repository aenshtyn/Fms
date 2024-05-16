from rest_framework import viewsets
from .models import Parcel, Usage, Maintenance, Paddock
from .serializers import ParcelSerializer, UsageSerializer, MaintenanceSerializer, PaddockSerializer

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class UsageViewSet(viewsets.ModelViewSet):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
class PaddockViewSet(viewsets.ModelViewSet):
    queryset = Paddock.objects.all()
    serializer_class = PaddockSerializer
