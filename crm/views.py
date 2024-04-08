from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status, mixins, viewsets

from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

  