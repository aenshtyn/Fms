from django.shortcuts import render
from rest_framework import status, viewsets

# Create your views here.
class FinanceViewSet(viewsets.ModelViewSet):

    def list(self, request):
        pass