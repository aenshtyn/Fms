# finance/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialTransactionViewSet, ExpenseViewSet, RevenueViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'financial-transactions', FinancialTransactionViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'revenues', RevenueViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
