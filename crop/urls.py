from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from .views import CropViewSet


router = DefaultRouter()
router.register(r'crops', CropViewSet, basename = 'crops')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]