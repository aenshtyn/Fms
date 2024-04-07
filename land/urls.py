from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import LandViewSet


router = DefaultRouter()
router.register(r'land', LandViewSet, basename = 'Land')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]