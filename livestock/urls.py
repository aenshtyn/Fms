from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet, HealthViewSet, BreedingViewSet, ReproductionViewSet, VaccinationViewSet, MortalityViewSet

router = DefaultRouter()

router.register(r'animals/(?<species>\w+)', AnimalViewSet, basenmae='animal')
router.register(r'health', HealthViewSet)
router.register(r'breeding', BreedingViewSet)
router.register(r'reproduction', ReproductionViewSet)
router.register(r'vaccination', VaccinationViewSet)
router.register(r'mortality', MortalityViewSet)

urlpatterns = [
    path('', include(router.urls)),

]