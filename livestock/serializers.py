from rest_framework import serializers
from .models import Animal, Health, Breeding, Reproduction, Vaccination, Mortality
from dairy.serializers import MilkProductionSerializer

class AnimalSerializer(serializers.ModelSerializer):
    # calves = serializers.SerializerMethodField()
    # ai_records = serializers.SerializerMethodField()
    # calvings = serializers.SerializerMethodField()
    # treatments = serializers.SerializerMethodField()
    # parents = serializers.SerializerMethodField()
    # milk_production = serializers.SerializerMethodField()
    class Meta:
        model = Animal
        fields = '__all__'

    # def get_calves

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = '__all__'

class BreedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeding
        fields = 'animal','expected_due_date'

class ReproductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reproduction
        fields = '__all__'

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'

class MortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortality
        fields = '__all__'