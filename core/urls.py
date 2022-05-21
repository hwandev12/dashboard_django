from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("design/", include("apps.home.urls")),
    path("", include("apps.base.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
