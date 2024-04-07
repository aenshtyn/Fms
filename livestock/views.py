from rest_framework import viewsets
from .models import Livestock, Health, Breeding, Reproduction, Vaccination, Mortality
from .serializers import LivestockSerializer, HealthSerializer, BreedingSerializer, ReproductionSerializer, VaccinationSerializer, MortalitySerializer

class LivestockViewSet(viewsets.ModelViewSet):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer

class HealthViewSet(viewsets.ModelViewSet):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer

class BreedingViewSet(viewsets.ModelViewSet):
    queryset = Breeding.objects.all()
    serializer_class = BreedingSerializer

class ReproductionViewSet(viewsets.ModelViewSet):
    queryset = Reproduction.objects.all()
    serializer_class = ReproductionSerializer

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer

class MortalityViewSet(viewsets.ModelViewSet):
    queryset = Mortality.objects.all()
    serializer_class = MortalitySerializer