from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import ProcurementViewSet


router = DefaultRouter()
router.register(r'procurement', ProcurementViewSet, basename = 'Procurement')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]