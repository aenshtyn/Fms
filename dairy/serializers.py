from rest_framework import serializers
from .models import Production, Feeds
from livestock.models import Animal

class ProductionSerializer(serializers.ModelSerializer):
    cow_id = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(),source='cow', write_only=True)
    # cow = serializers.CharField(source='cow.id_number', read_only=True)
    # cow = serializers.ReadOnlyField(source='cow.id_number')
    # total_volume = serializers.SerializerMethodField()

    class Meta:
        model = Production
        fields = ['cow_id', 'milking_date', 'morning_volume', 'evening_volume']
        # read_only_fields = ['total_volume']

    # def get_total_volume(self, obj):
    #     return obj.morning_volume + obj.evening_volume
    
    def create(self, validated_data):
        
        cow=validated_data.pop('cow', None)

        if cow is None:
            raise serializers.ValidationError("Cow ID is required.")
        # Custom create method to handle the creation of a production record
        production = Production(**validated_data,
            cow=cow)
        #     milking_date=validated_data['milking_date'],
        #     morning_volume=validated_data['morning_volume'],
        #     evening_volume=validated_data['evening_volume']
        # )
        production.save()
        return production

class FeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = '__all__'

class LactatingAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = 'id_number', 'delivery_date'