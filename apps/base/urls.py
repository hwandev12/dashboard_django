from django.contrib.auth import views as auth_views
from django.urls import path
from apps.base import views
from .forms import *
from .views import SignupView, LoginView, profile

app_name = 'phone'

urlpatterns = [
    path('', views.base_home, name='base_home'),
    path('base/signup/', SignupView.as_view(), name='base_registration'),
    path('base/login/', LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                          authentication_form=LoginForm), name='base_login'),
    path('base/logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='base_logout'),
    path('profile/', profile, name='users-profile'),
]
