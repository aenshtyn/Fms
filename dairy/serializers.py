from rest_framework import serializers
from .models import MilkProduction

class DairySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MilkProduction
        fields = '__all__'