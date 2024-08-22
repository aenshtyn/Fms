from rest_framework import serializers
from .models import Crop, CropCycle, CropHealth, Harvest, PestControl

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class CropCycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCycle
        fields = '__all__'

class CropHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropHealth
        fields = '__all__'

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = '__all__'

class PestControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = PestControl
        fields = '__all__'