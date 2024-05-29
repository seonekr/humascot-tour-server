
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tourapi/", include("tourApi.urls")),
    path("users/", include("users.urls")),
    path("", include_docs_urls(title="Tour APIs") ),
    path(
        "schema",
        get_schema_view(
            title="Tour APIs",
            description="APIs for Humascot Tour",
            version="1.0.0",
        ),
        name="openapi-shecma",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 