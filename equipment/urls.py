from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import EquipmentViewSet


router = DefaultRouter()
router.register(r'equipment', EquipmentViewSet, basename = 'Equipment')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]