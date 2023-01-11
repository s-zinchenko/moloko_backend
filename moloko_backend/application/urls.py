from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django_serializer.v2.swagger.views import index as swagger_index





urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path("swagger.json", swagger_index),
                path(
                    "core.",
                    include("moloko_backend.core.urls"),
                ),
                path(
                    "news.",
                    include("moloko_backend.news.urls"),
                ),
                path(
                    "cooperation.",
                    include("moloko_backend.cooperation.urls"),
                ),
                path(
                    "bids.",
                    include("moloko_backend.bids.urls"),
                ),
            ]
        ),
    ),
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

if settings.SILK:
    urlpatterns += [
        re_path(r"silk/", include("silk.urls", namespace="silk")),
    ]
