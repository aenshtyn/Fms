from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views

from .views import CategoryViewSet, ProductViewSet, StockViewSet, TransactionViewSet



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    # Employees
    path('', include(router.urls)),

]