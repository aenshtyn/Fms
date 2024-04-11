from rest_framework import serializers
from .models import Parcel, Usage, Maintenance, User

class UsageSerializer(serializers.ModelSerializer):
    parcel = serializers.ReadOnlyField(source = 'parcel.parcel_number')
    class Meta:
        model = Usage
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    usage_history = UsageSerializer(many=True, read_only=True)
    maintenance_history = MaintenanceSerializer(many=True, read_only=True)
    class Meta:
        model = Parcel        
        fields = 'parcel_number','owner', 'size', 'description', 'usage_history', 'maintenance_history'