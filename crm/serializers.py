from rest_framework import serializers
from .models import Crm

class CrmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crm
        fields = '__all__'