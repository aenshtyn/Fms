from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views
from .views import LivestockViewSet

router = DefaultRouter()

router.register(r'livestock', LivestockViewSet, basename='livestock')

urlpatterns = [
    path('', include(router.urls)),

]