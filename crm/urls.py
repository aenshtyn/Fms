from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import ClientViewSet

router = DefaultRouter()
router.register(r'crm', ClientViewSet, basename='Clients')

urlpatterns = [
    # Clients
    path('', include(router.urls)),

]