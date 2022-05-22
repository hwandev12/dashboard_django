from django.urls import path
from apps.base import views
from .views import SignupView
from django.contrib.auth.views import *

app_name = 'phone'

urlpatterns = [
    path('', views.base_home, name='base_home'),
    path('signup/', SignupView.as_view(), name='registration')
]
