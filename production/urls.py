from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import ProductionViewSet


router = DefaultRouter()
router.register(r'production', ProductionViewSet, basename='Production')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]