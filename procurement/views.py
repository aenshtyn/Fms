from django.shortcuts import render
from rest_framework import status, viewsets
# Create your views here.
class ProcurementViewSet(viewsets.ModelViewSet):

    def list(self, request):
        pass