from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views


router = DefaultRouter()


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]