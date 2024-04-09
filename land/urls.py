from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParcelViewSet, UsageViewSet, MaintenanceViewSet

router = DefaultRouter()
router.register(r'parcels', ParcelViewSet)
router.register(r'usage', UsageViewSet)
router.register(r'maintenance', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
