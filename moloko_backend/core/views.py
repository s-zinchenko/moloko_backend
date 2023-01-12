from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from django_serializer.v2.views import ApiView, HttpMethod, ListApiView

from moloko_backend.core.models import Company, Management
from moloko_backend.core.serializers import AboutCompanySerializer, ManagementListSerializer


class AboutCompanyView(ApiView):
    class Meta:
        model = Company
        method = HttpMethod.GET
        serializer = AboutCompanySerializer
        tags = ["core"]

    def execute(self, request: WSGIRequest, *args: Any, **kwargs: Dict[Any, Any]) -> Dict[Any, Any]:
        obj = Company.objects.prefetch_related("fact_set").get()
        return obj


class ManagementListView(ListApiView):
    class Meta:
        model = Management
        serializer = ManagementListSerializer
        tags = ["core"]

    def execute(self, request, *args, **kwargs):
        qs = super().execute(request, *args, **kwargs)
        return {"management": qs}
