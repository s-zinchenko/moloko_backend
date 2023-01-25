from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from django_serializer.v2.views import ApiView, HttpMethod

from moloko_backend.core.models import Company, Agreement
from moloko_backend.core.serializers import (
    AboutCompanySerializer,
    GetAgreementSerializer,
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


class GetAgreementView(ApiView):
    class Meta:
        model = Agreement
        method = HttpMethod.GET
        serializer = GetAgreementSerializer
        tags = ["core"]
