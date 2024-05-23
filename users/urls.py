from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
# from .views import send_analytics_view, send_message_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('send_message/', send_message_view, name='send_message'),
    # path('send_analytics/', send_analytics_view, name='send_analytics'),
    # # other routes
]
