from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from .views import CropViewSet, CropCycleViewSet, CropHealthViewSet, HarvestViewSet, PestControlViewSet


router = DefaultRouter()
router.register(r'crops', CropViewSet, basename='crop')
router.register(r'crop-cycles', CropCycleViewSet, basename='crop-cycle')
router.register(r'crop-health', CropHealthViewSet, basename='crop-health')
router.register(r'harvests', HarvestViewSet, basename='harvest')
router.register(r'pest-control', PestControlViewSet, basename='pest-control')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]