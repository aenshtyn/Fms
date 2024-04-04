from django.urls import path
from app import views

urlpatterns = [
    path("workers", views.workers_list, name='workers'),
    path("analytics/workers", views.workers_analytics, name='workers_analytics'),
]