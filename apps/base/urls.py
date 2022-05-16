from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.base_home, name='base_home'),
]
