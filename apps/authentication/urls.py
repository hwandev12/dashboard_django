from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView
)

app_name = 'authentication'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('password-reset-view/', PasswordResetView.as_view(), name='password-reset-view')
]
