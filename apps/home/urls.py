from django.urls import path, re_path
from apps.home import views

app_name = 'home'

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('billing/', views.billing, name='billing'),
    path('table/', views.tables, name='tables'),
    path('virtual-reality/', views.virtual_reality, name='virtual_reality'),
    path('EUUjphcxKmD7qf/rtl-section/', views.rtl, name='rtl_section')
    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
