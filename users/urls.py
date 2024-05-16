from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterInvitedUser, FarmViewSet, InvitationViewSet, UserViewSet, send_message_view, send_analytics_view

router = DefaultRouter()
router.register(r'farms', FarmViewSet)
router.register(r'invitations', InvitationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/<str:token>/', RegisterInvitedUser.as_view(), name='register-invited-user'),
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),  # Required for allauth
    path('send_message/', send_message_view, name='send_message'),
    path('send_analytics/', send_analytics_view, name='send_analytics'),
    # other routes
]
