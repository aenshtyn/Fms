from rest_framework import viewsets, status, request
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Production, Feeds
from .serializers import ProductionSerializer, FeedsSerializer
from livestock.serializers import AnimalSerializer
from livestock.models import Animal
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import F, Sum
from django.shortcuts import get_object_or_404
import json

class ProductionViewSet(viewsets.ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

    @action(detail=False, methods=['post'])
    def save(self, request):
        milking_date = request.data.get('milking_date')
        milk_records = request.data.get('milk_records', [])

        if not milking_date:
            return Response({"milking_date": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        new_productions = []

        for record in milk_records:
            record['milking_date'] = request.data.get('milking_date')
            serializer = ProductionSerializer(data=record)
            if serializer.is_valid():
                # Prepare data for bulk creation
                validated_data = serializer.validated_data
                
                animal = get_object_or_404(Animal, id=validated_data['cow'])

                new_productions.append(Production(
                    cow=animal.id,
                    milking_date=validated_data['milking_date'],
                    morning_volume=validated_data['morning_volume'],
                    evening_volume=validated_data['evening_volume']
                ))
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Bulk create all valid production records
        Production.objects.bulk_create(new_productions)
        return Response({'message': 'Milk records saved successfully'}, status=status.HTTP_201_CREATED)

    # @action(detail=False, methods=['post'])
    # def save(self, request):
        milking_date = request.data.get('milkingDate')
        records = request.data.get('records', [])
        
        new_productions = []
        for record in records:
            animal = get_object_or_404(Animal, id=record['cow_id'])
            production_data = {
                'cow': animal,
                'milking_date': milking_date,
                'morning_volume': record['morning_volume'],
                'evening_volume': record['evening_volume']
            }
            serializer = ProductionSerializer(data=production_data)
            if serializer.is_valid():
                new_productions.append(serializer.save(commit=False))
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        Production.objects.bulk_create(new_productions)
        return Response({'message': 'Milk records saved successfully'}, status=status.HTTP_201_CREATED)
    
    # @action(detail=False, methods=['post'])
    # def save(self, request):
        milk_records = request.data.get('milk_records', [])
        
        # Prepare a list to hold new production records
        new_productions = []
        
        for record in milk_records:
            # Use DRF's serializer to validate and deserialize input
            serializer = ProductionSerializer(data=record)
            if serializer.is_valid():
                # Instead of creating each instance, prepare it for bulk creation
                validated_data = serializer.validated_data
                animal = get_object_or_404(Animal, id=validated_data['cow'].id)
                new_productions.append(Production(
                    cow=animal,
                    milking_date=validated_data['milking_date'],
                    morning_volume=validated_data['morning_volume'],
                    evening_volume=validated_data['evening_volume']
                ))
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Bulk create all valid production records
        Production.objects.bulk_create(new_productions)
        
        return Response({'message': 'Milk records saved successfully'}, status=status.HTTP_201_CREATED)
    
    # @action(detail=False, methods=['post'])
    # def save(self, request):
        
    #     if request.method == 'POST':
    #         # Parse the JSON data sent from the frontend
    #         try:
    #             data = json.loads(request.body)
    #         except json.JSONDecodeError:
    #             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
            
    #         # Extract milk records for each animal from the data
    #         milk_records = data.get('milk_records', [])
            
    #         # Loop through the milk records and save them
    #         for record in milk_records:
    #             milking_date = record.get('milking_date')
    #             animal_id = record.get('animal_id')
    #             morning_volume = record.get('morning_volume')
    #             evening_volume = record.get('evening_volume')

    #             animal = Animal.objects.get(id=animal_id)
                
    #             # Create a MilkRecord instance and save it to the database
    #             Production.objects.create(
    #                 milking_date=milking_date,
    #                 cow=animal,
    #                 morning_volume=morning_volume,
    #                 evening_volume=evening_volume
    #             )
            
    #         return JsonResponse({'message': 'Milk records saved successfully'}, status=200)
    #     else:
    #         return JsonResponse({'error': 'Method not allowed'}, status=405)
        

    @action(detail=False, methods=['put'])
    def edit(self, request):
        if request.method == 'PUT':
            # Parse the JSON data sent from the frontend
            try:
                data = request.data
            except ValueError:
                return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Extract milk records for each animal from the data
            milk_records = data.get('milk_records', [])
            
            # Loop through the milk records and save them
            for record in milk_records:
                milking_date = record.get('milking_date')
                animal_id = record.get('animal_id')
                morning_volume = record.get('morning_volume')
                evening_volume = record.get('evening_volume')

                try:
                    milk_record = Production.objects.get(milking_date=milking_date, cow__id=animal_id)
                except Production.DoesNotExist:
                    return Response({'error': 'Milk record does not exist'}, status=status.HTTP_404_NOT_FOUND)
                
                # Create a MilkRecord instance and save it to the database
                milk_record.morning_volume = morning_volume
                milk_record.evening_volume = evening_volume
                milk_record.save()
                
            
            return JsonResponse({'message': 'Milk records updated successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

    # @action(detail=False, methods=['post'])
    def add_multiple_milk_records(request):
        records_data = request.data.get('records', [])

    # Validate and save each record
        saved_records = []
        errors = []
        for record_data in records_data:
            serializer = ProductionSerializer(data=record_data)
            if serializer.is_valid():
                saved_record = serializer.save()
                saved_records.append(saved_record)
            else:
                errors.append(serializer.errors)

        if errors:
            # Return errors if any records failed validation
            return JsonResponse({'errors': errors}, status=400)
        else:
            # Return the saved records
            serialized_data = ProductionSerializer(saved_records, many=True).data
            return JsonResponse({'records': serialized_data}, status=201)

    @action(detail=False, methods=['get'])
    def animals(self, request, format=None):
        lactating_animals = Animal.get_lactating_cows()
        serializer = AnimalSerializer(lactating_animals, many=True)
        return Response(serializer.data)
    
    # @action(detail=False, methods=['get'])
    # def daily(self, request):
    #     total_volumes = Production.Production.objects.values('milking_date').annotate(total_volume=Sum('morning_volume') + Sum('evening_volume'))
    #     serializer = ProductionSerializer(total_volumes, many=True)

    #     return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def daily(self, request):
        # Get all unique milking dates
        milking_dates = Production.objects.values_list('milking_date', flat=True).order_by('-milking_date').distinct()

        total_volumes_per_day = []
        for date in milking_dates:
            daily_volumes = Production.objects.filter(milking_date=date).aggregate(
            total_morning_volume=Sum('morning_volume'),
            total_evening_volume=Sum('evening_volume')
        )
            total_volume = daily_volumes.get('total_morning_volume', 0) + daily_volumes.get('total_evening_volume', 0)

            total_volumes_per_day.append({
                'milking_date': date,
                'morning_volume': daily_volumes.get('total_morning_volume', 0),
                'evening_volume': daily_volumes.get('total_evening_volume', 0),
                'total_volume': total_volume,
            })

        serializer = ProductionSerializer(total_volumes_per_day, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def monthly(self, request, year, month):

        if year is None or month is None:
            return Response({'error': 'Year and month parameters are required'}, status=status.HTTP_400_BAD_REQUEST)

        total_morning_volume, total_evening_volume, total_monthly_volume = Production.month_total_volume(year, month)

        data = {
            'year': year,
            'month': month,
            'morning_volume': total_morning_volume,
            'evening_volume': total_evening_volume,
            'total_volume': total_monthly_volume
        }

        serializer = ProductionSerializer(data)
        return Response(serializer.data)


class FeedsViewSet(viewsets.ModelViewSet):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer