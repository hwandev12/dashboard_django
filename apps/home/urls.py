from django.urls import path, re_path
from apps.home import views

app_name = 'home'

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('billing/', views.billing, name='billing'),
    path('table/', views.tables, name='tables')
    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
