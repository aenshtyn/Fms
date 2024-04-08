from rest_framework import serializers
from .models import Animal, Health, Breeding, Reproduction, Vaccination, Mortality
from dairy.models import MilkProduction

class AnimalSerializer(serializers.ModelSerializer):
    # calves = serializers.SerializerMethodField()
    # ai_records = serializers.SerializerMethodField()
    # calvings = serializers.SerializerMethodField()
    # treatments = serializers.SerializerMethodField()
    # parents = serializers.SerializerMethodField()
    milk_production = serializers.SerializerMethodField()
    # production = MilkProductionSerializer()
    class Meta:
        model = Animal
        # fields = '__all__'
        fields = 'id_number','age', 'milk_production'

    def get_milk_production(self, obj):
        total_production = MilkProduction.objects.filter(cow=obj).aggregate(total_volume=Sum('morning_volume' + 'evening_volume'))['total_volume']
        return total_production or 0

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