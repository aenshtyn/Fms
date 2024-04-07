from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import CrmViewSet

router = DefaultRouter()
router.register(r'crm', CrmViewSet, basename='Crms')

urlpatterns = [
    # Crms
    path('', include(router.urls)),

]