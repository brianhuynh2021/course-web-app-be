from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from .views import RegisterView, LogoutView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token_refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), name="logout")
]
