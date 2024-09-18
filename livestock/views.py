from rest_framework import viewsets
from django.db.models import Prefetch
from dairy.models import Production
from .models import Animal, Health, Breeding, Reproduction, Vaccination, Mortality
from .serializers import AnimalSerializer, HealthSerializer, BreedingSerializer, ReproductionSerializer, VaccinationSerializer, MortalitySerializer

class CowViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.filter(species='cow')
    serializer_class = AnimalSerializer

    def get_queryset(self):
        # Customize the prefetch to limit the productions fetched
        return self.queryset.prefetch_related(
            Prefetch(
                'productions',
                queryset=Production.objects.order_by('-milking_date')[:10],
                to_attr='latest_productions'
            )
        )
    
class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer

    def get_queryset(self):
        # Get the species from the request (query parameter or URL)
        species = self.kwargs.get('species', None)

        # Filter by species if provided, otherwise return all animals
        queryset = Animal.objects.all()

        # Prefetch the latest 10 milk productions for each animal
        if species == 'cow':
            queryset.prefetch_related(
                Prefetch(
                    'productions',
                    queryset=Production.objects.order_by('-milking_date')[:10],
                    to_attr='latest_productions'
            )
        )
        if species:
            queryset = queryset.filter(species=species)

            return queryset

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