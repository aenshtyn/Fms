from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import MilkProductionViewSet, DairyFeedsViewSet


router = DefaultRouter()
router.register(r'milk-productions', MilkProductionViewSet)
router.register(r'dairy-feeds', DairyFeedsViewSet)


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]