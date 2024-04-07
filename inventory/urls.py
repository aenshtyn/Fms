from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import InventoryViewSet


router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename = 'Inventory')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]