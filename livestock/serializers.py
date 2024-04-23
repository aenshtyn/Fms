from rest_framework import serializers
from .models import Animal, Health, Breeding, Reproduction, Vaccination, Mortality
from dairy.models import Production
from django.db.models import Sum

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health
        fields = 'date', 'condition'

class BreedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeding
        fields = 'animal','expected_due_date'

class ProductionSerializer(serializers.ModelSerializer):
    total_volume = serializers.SerializerMethodField()

    class Meta:
        model = Production
        fields = ['milking_date', 'total_volume']

    def get_total_volume(self, obj):
        return obj.morning_volume + obj.evening_volume


class AnimalSerializer(serializers.ModelSerializer):
    health_records = HealthSerializer(many=True, read_only=True)
    breedings = BreedingSerializer(many=True, read_only=True)
    milk_productions = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = ['id','id_number', 'species', 'breed', 'date_of_birth', 'health_records', 'breedings', 'milk_productions']


    def get_milk_productions(self, obj):
        if hasattr(obj, 'latest_productions'):
            return ProductionSerializer(obj.latest_productions, many=True).data
        else:
            productions = Production.objects.filter(cow=obj).order_by('-milking_date')[:10]
            return ProductionSerializer(productions, many=True).data


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