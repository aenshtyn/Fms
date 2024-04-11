from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MilkProduction, DairyFeeds
from .serializers import MilkProductionSerializer, DairyFeedsSerializer
from livestock.serializers import AnimalSerializer
from livestock.models import Animal

class MilkProductionViewSet(viewsets.ModelViewSet):
    queryset = MilkProduction.objects.all()
    serializer_class = MilkProductionSerializer

    @action(detail=False, methods=['get'])
    def lactating_animals(self, request, *args, **kwargs):
        lactating_animals = Animal.objects.filter(milkproduction__isnull=False).distinct()
        serializer = AnimalSerializer(lactating_animals, many=True)
        return Response(serializer.data)



class DairyFeedsViewSet(viewsets.ModelViewSet):
    queryset = DairyFeeds.objects.all()
    serializer_class = DairyFeedsSerializer