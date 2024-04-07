from rest_framework import serializers
from .models import Livestock, HealthRecord, BreedingRecord, ReproductionRecord, VaccinationRecord, MortalityRecord

class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = '__all__'

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class BreedingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreedingRecord
        fields = '__all__'

class ReproductionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReproductionRecord
        fields = '__all__'

class VaccinationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = '__all__'

class MortalityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MortalityRecord
        fields = '__all__'