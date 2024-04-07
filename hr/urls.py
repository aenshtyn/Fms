from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import HrViewSet


router = DefaultRouter()
router.register(r'hr', HrViewSet, basename = 'Hr')


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]