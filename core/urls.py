from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import random, string

x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),
    path(x, include("apps.home.urls", namespace='developer')),
    path("", include("apps.base.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
