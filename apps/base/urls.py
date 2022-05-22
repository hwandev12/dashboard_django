from django.urls import path
from apps.base import views
from .forms import *
from .views import SignupView, LoginView

app_name = 'phone'

urlpatterns = [
    path('', views.base_home, name='base_home'),
    path('base/signup/', SignupView.as_view(), name='base_registration'),
    path('base/login/', LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                          authentication_form=LoginForm), name='base_login'),
]
