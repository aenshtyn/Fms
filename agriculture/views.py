from rest_framework import viewsets
from .models import Crop, CropCycle, CropHealth, Harvest, PestControl
from .serializers import CropSerializer, CropCycleSerializer, CropHealthSerializer, HarvestSerializer, PestControlSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class CropCycleViewSet(viewsets.ModelViewSet):
    queryset = CropCycle.objects.all()
    serializer_class = CropCycleSerializer

class CropHealthViewSet(viewsets.ModelViewSet):
    queryset = CropHealth.objects.all()
    serializer_class = CropHealthSerializer

class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

class PestControlViewSet(viewsets.ModelViewSet):
    queryset = PestControl.objects.all()
    serializer_class = PestControlSerializer