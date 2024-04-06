from rest_framework import serializers
from app.models import Livestock

class LivestockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livestock
        fields = '__all__'