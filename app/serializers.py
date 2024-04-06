from rest_framework import serializers
from app.models import Employee, Feed, Crop, Inventory, FeedConsumption

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feed
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crop
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventory
        fields = '__all__'