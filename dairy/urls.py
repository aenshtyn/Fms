from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import ProductionViewSet, FeedsViewSet


router = DefaultRouter()
router.register(r'production', ProductionViewSet)
router.register(r'feeds', FeedsViewSet)


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]