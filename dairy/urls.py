from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import MilkProductionViewSet


router = DefaultRouter()
router.register(r'dairy', MilkProductionViewSet, basename = 'Dairy')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]