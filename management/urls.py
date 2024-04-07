from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import ManagementViewSet


router = DefaultRouter()
router.register(r'management', ManagementViewSet, basename = 'Management')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]