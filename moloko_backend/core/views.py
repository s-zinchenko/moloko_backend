from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from django_serializer.v2.views import ApiView, HttpMethod

from moloko_backend.core.models import Company
from moloko_backend.core.serializers import (
    AboutCompanySerializer,
)


class AboutCompanyView(ApiView):
    class Meta:
        model = Company
        method = HttpMethod.GET
        serializer = AboutCompanySerializer
        tags = ["core"]

    def execute(
        self, request: WSGIRequest, *args: Any, **kwargs: Dict[Any, Any]
    ) -> Dict[Any, Any]:
        obj = Company.objects.prefetch_related("fact_set").get()
        return obj
