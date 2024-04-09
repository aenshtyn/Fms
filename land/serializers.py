from rest_framework import serializers
from .models import Parcel, Usage, Maintenance

class UsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usage
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    usage = UsageSerializer(many=True, read_only=True)
    maintenance = MaintenanceSerializer(many=True, read_only=True)

    class Meta:
        model = Parcel
        fields = '__all__'
