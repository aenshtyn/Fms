from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, TaskViewSet, LeaveViewSet, OnboardingViewSet, AttendanceViewSet, RecruitmentViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'leaves', LeaveViewSet, basename='leaves')
router.register(r'onboarding', OnboardingViewSet, basename='onboarding')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'recruitment', RecruitmentViewSet, basename='recruitment')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]