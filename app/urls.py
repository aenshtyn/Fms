from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from .views import EmployeeViewSet, LivestockViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'livestock', LivestockViewSet, basename='livestock')

urlpatterns = [
    # Employees
    path('', include(router.urls)),


    # analytics
    path("analytics/Employees", views.Employees_analytics, name='Employees_analytics'),
]