from rest_framework import serializers
from .models import MilkProduction, DairyFeeds
from livestock.models import Animal

class MilkProductionSerializer(serializers.ModelSerializer):
    total_volume = serializers.SerializerMethodField()
    cow = serializers.ReadOnlyField(source='animal.id_number')

    class Meta:
        model = MilkProduction
        fields = ['id', 'cow', 'milking_date', 'morning_volume', 'evening_volume', 'total_volume']
        read_only_fields = ['total_volume']

    def get_total_volume(self, obj):
        return obj.morning_volume + obj.evening_volume

class DairyFeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DairyFeeds
        fields = '__all__'
