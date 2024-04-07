from rest_framework import viewsets
from .models import MilkProduction, DairyFeeds
from .serializers import MilkProductionSerializer, DairyFeedsSerializer

class MilkProductionViewSet(viewsets.ModelViewSet):
    queryset = MilkProduction.objects.all()
    serializer_class = MilkProductionSerializer

class DairyFeedsViewSet(viewsets.ModelViewSet):
    queryset = DairyFeeds.objects.all()
    serializer_class = DairyFeedsSerializer