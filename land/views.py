from django.shortcuts import render
from rest_framework import status, viewsets

# Create your views here.
class LandViewSet(viewsets.ModelViewSet):

    def list(self, request):
        pass