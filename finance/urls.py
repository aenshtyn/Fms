from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import FinanceViewSet


router = DefaultRouter()
router.register(r'finance', FinanceViewSet, basename = 'Finance')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]