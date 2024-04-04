from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from app.models import Worker
from app.serializers import WorkerSerializer

@api_view(['GET', 'POST', 'DELETE'])
def workers_list(request):
    if request.method == 'GET':
        workers = Worker.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            workers = workers.filter(name__icontains=name)
        worker_serializer = WorkerSerializer(workers, many=True)
        return JsonResponse(worker_serializer.data, safe=False)
# Create your views here.


@api_view(['GET'])
def workers_analytics(request):
    total_workers = Worker.objects.all().count()

    data = {
        'total_workers': total_workers,
    }

    return JsonResponse(data)