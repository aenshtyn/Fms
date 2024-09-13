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
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import TruncWeek, TruncMonth , TruncDay
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth


class ProductionViewSet(viewsets.ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer

    @action(detail=False, methods=['post'])
    def save(self, request):
        milking_date = request.data.get('milking_date')
        milk_records = request.data.get('milk_records', [])

        for record in milk_records:
            cow_id = record.get('cow_id')
            morning_volume = record.get('morning_volume', 0.0)
            evening_volume = record.get('evening_volume', 0.0)

            cow = Animal.objects.get(id_number=cow_id)
            production, created = Production.objects.get_or_create(
                cow=cow,
                milking_date=milking_date,
                defaults={'morning_volume': morning_volume, 'evening_volume' : evening_volume }
            )

            if not created: 
                production.morning_volume = morning_volume
                production.evening_volume = evening_volume
                production.save()

        return Response({"message": "Records saved successfully"}, status=status.HTTP_201_CREATED)
    

    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        date = request.query_params.get('date')
        if date:
            milk_records = Production.objects.filter(milking_date=date)
            serializer = ProductionSerializer(milk_records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Date parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
  

        # Bulk create all valid pro    

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

    @action(detail=False, methods=['get'])
    def animals(self, request, format=None):
        lactating_animals = Animal.get_lactating_cows()
        serializer = AnimalSerializer(lactating_animals, many=True)
        return Response(serializer.data)
    
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
    def monthly(self, request):

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

    @action(detail=False, methods=['get'])
    def analytics(self, request, format=None):
        today = timezone.now().date()
        last_week = today - timedelta(days=7)

        # Calculate total volumes for today
        total_day_morning_volume, total_day_evening_volume, total_day_volume = Production.day_total_volume(today)

        # Calculate last week's volumes
        last_week_volumes = Production.objects.filter(milking_date__range=(last_week, today)).aggregate(
            total_morning_volume=Sum('morning_volume'),
            total_evening_volume=Sum('evening_volume')
        )

        last_week_morning_volume = last_week_volumes['total_morning_volume'] or 0
        last_week_evening_volume = last_week_volumes['total_evening_volume'] or 0
        last_week_total_volume = last_week_morning_volume + last_week_evening_volume

        # Calculate changes
        morning_volume_change = (total_day_morning_volume - (last_week_morning_volume / 7)) / (last_week_morning_volume / 7) * 100 if last_week_morning_volume else 0
        evening_volume_change = (total_day_evening_volume - (last_week_evening_volume / 7)) / (last_week_evening_volume / 7) * 100 if last_week_evening_volume else 0
        total_volume_change = (total_day_volume - (last_week_total_volume / 7)) / (last_week_total_volume / 7) * 100 if last_week_total_volume else 0

        data = {
            'total_day_morning_volume': total_day_morning_volume,
            'total_day_evening_volume': total_day_evening_volume,
            'total_day_volume': total_day_volume,
            'last_week_morning_volume': last_week_morning_volume,
            'last_week_evening_volume': last_week_evening_volume,
            'morning_volume_change': morning_volume_change,
            'evening_volume_change': evening_volume_change,
            'total_volume_change': total_volume_change,
        }

        return Response(data)
    
    # @action(detail=False, methods=['get'])
    # def milk_trends(self, request, format=None):
    #     today = timezone.now().date()
    #     twelve_months_ago = today - timedelta(days=365)

    #     # Aggregate milk production by week for the last twelve months
    #     weekly_data = Production.objects.filter(milking_date__gte=twelve_months_ago).annotate(
    #         week=TruncWeek('milking_date'),
    #         month=TruncMonth('milking_date')
    #     ).values('week', 'month').annotate(
    #         total_morning_volume=Sum('morning_volume'),
    #         total_evening_volume=Sum('evening_volume')
    #     ).order_by('month', 'week')

    #     # Prepare data for the graph
    #     monthly_trends = {}
    #     for entry in weekly_data:
    #         month = entry['month'].strftime('%m')
    #         if month not in monthly_trends:
    #             monthly_trends[month] = []
    #         total_volume = (entry['total_morning_volume'] or 0) + (entry['total_evening_volume'] or 0)
    #         monthly_trends[month].append({
    #             'week': entry['week'].strftime('%W'),  # Year-Week format
    #             'total_volume': total_volume
    #         })

    #     return Response(monthly_trends)
    

    @action(detail=False, methods=['get'])
    def milk_trends(self, request, format=None):
        today = timezone.now().date()
        one_year_ago = today - timedelta(days=365)

        # Define month labels for converting numeric month to string
        month_labels = {
            1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
            7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
        }

        # Aggregate milk production by day for the last twelve months
        daily_data = Production.objects.filter(
            milking_date__gte=one_year_ago
        ).annotate(
            day=TruncDay('milking_date'),
            month=ExtractMonth('milking_date')
        ).values('day', 'month').annotate(
            total_volume=Sum('morning_volume') + Sum('evening_volume')
        ).order_by('month', 'day')

        # Prepare data for the graph, grouping by months
        production_trends = {}
        for entry in daily_data:
            month_name = month_labels.get(entry['month'], "Unknown Month")  # Get month name from month number
            if month_name not in production_trends:
                production_trends[month_name] = []
            production_trends[month_name].append({
                'date': entry['day'].day,  # Just the day part
                'total_volume': entry['total_volume']
            })

        return Response(production_trends)
    

# @action(detail=False, methods=['get'])
#     def milk_trends(self, request, format=None):
#         today = timezone.now().date()
#         one_year_ago = today - timedelta(days=365)

#         #  Define month labels for converting numeric month to string
#         month_labels = {
#             1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
#             7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
#         }

#         # Aggregate milk production by day for the last twelve months
#         daily_data = Production.objects.filter(
#             milking_date__gte=one_year_ago
#         ).annotate(
#             day=TruncDay('milking_date'),
#             month=ExtractMonth('milking_date')
#         ).values('day', 'month').annotate(
#             total_volume=Sum('morning_volume') + Sum('evening_volume')
#         ).order_by('month', 'day')

#         # Prepare data for the graph, grouping by months
#         production_trends = {}
#         for entry in daily_data:
#             month_name = month_lables.get(entry['day'].strftime('%B')  # Get the month name from the date
#             if month_name not in production_trends:
#                 monthly_trends[month_name] = []
#             monthly_trends[month_name].append({
#                 'date': entry['day'].day,  # Just the day part
#                 'total_volume': entry['total_volume']
#             })

#         return Response(production_trends)


    # @action(detail=False, methods=['get'])
    # def milk_trends(self, request, format=None):
    #     today = timezone.now().date()
    #     # twelve_months_ago = today - timedelta(days=365)
    #     one_year_ago = today - timedelta(days=365)

    #     # Define month labels for converting numeric month to string
    #     month_labels = {
    #         1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    #         7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    #     }


    #     # Aggregate milk production by day for the last twelve months
    #     daily_data = Production.objects.filter(milking_date__gte=one_year_ago).annotate(
    #         day=TruncDay('milking_date')
    #     ).values('day').annotate(
    #         total_volume=Sum('morning_volume') + Sum('evening_volume')
    #     ).order_by('day')


    #     # Aggregate milk production by week for the last twelve months
    #     # weekly_data = Production.objects.filter(milking_date__gte=twelve_months_ago).annotate(
    #     #     year=ExtractYear('milking_date'),
    #     #     week=ExtractWeek('milking_date'),
    #     #     month=ExtractMonth('milking_date')
    #     # ).values('year', 'week', 'month').annotate(
    #     #     total_morning_volume=Sum('morning_volume'),
    #     #     total_evening_volume=Sum('evening_volume')
    #     # ).order_by('year', 'month', 'week')

    #     formatted_data = []
    #     for entry in daily_data:
    #         formatted_data.append({
    #             'x': entry['day'].strftime('%Y-%m-%d'),  # Format date as Year-Month-Day
    #             'y': entry['total_volume']
    #         })

    #     # # Prepare data for the graph
    #     # monthly_trends = {}
    #     # for entry in weekly_data:
    #     #     month_name = month_labels.get(entry['month'], "Unknown Month")
    #     #     if month_name not in monthly_trends:
    #     #         monthly_trends[month_name] = []
    #     #     total_volume = (entry['total_morning_volume'] or 0) + (entry['total_evening_volume'] or 0)
    #     #     monthly_trends[month_name].append({
    #     #         'week': f"{entry['week']:02d}",
    #     #         'total_volume': total_volume
    #     #     })

    #     return Response(formatted_data)


    # @action(detail=False, methods=['get'])
    # def milk_trends(self, request, format=None):
    #     today = timezone.now().date()
    #     twelve_months_ago = today - timedelta(days=365)

    #     # Aggregate milk production by week for the last twelve months
    #     weekly_data = Production.objects.filter(milking_date__gte=twelve_months_ago).annotate(
    #         year=ExtractYear('milking_date'),
    #         week=ExtractWeek('milking_date')
    #     ).values('year', 'week').annotate(
    #         total_morning_volume=Sum('morning_volume'),
    #         total_evening_volume=Sum('evening_volume')
    #     ).order_by('year', 'week')

    #     # Prepare data for the graph
    #     trends_data = [
    #         {
    #             'week': f"{item['year']}{item['week']:02d}",
    #             'total_volume': (item['total_morning_volume'] or 0) + (item['total_evening_volume'] or 0)
    #         }
    #         for item in weekly_data
    #     ]

    #     return Response(trends_data)

class FeedsViewSet(viewsets.ModelViewSet):
    queryset = Feeds.objects.all()
    serializer_class = FeedsSerializer