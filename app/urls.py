from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')


urlpatterns = [
    # Employees
    path('', include(router.urls)),


    # analytics
    path("analytics/Employees", views.Employees_analytics, name='Employees_analytics'),
]