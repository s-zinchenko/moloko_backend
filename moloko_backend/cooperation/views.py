from django.db.models import QuerySet
from django_serializer.v2.views import ListApiView

from moloko_backend.cooperation.forms import TermsListForm
from moloko_backend.cooperation.models import (
    TermOfCooperation,
    Partner,
    Requirement,
)
from moloko_backend.cooperation.serializers import (
    TermsItemSerializer,
    PartnerItemSerializer,
    RequirementItemSerializer,
)


class TermsListView(ListApiView):
    class Meta:
        model = TermOfCooperation
        query_form = TermsListForm
        serializer = TermsItemSerializer
        tags = ["cooperation"]

    def get_queryset(self) -> QuerySet[TermOfCooperation]:
        return TermOfCooperation.objects.filter(type=self.request_query["type"])


class PartnersListView(ListApiView):
    class Meta:
        model = Partner
        serializer = PartnerItemSerializer
        tags = ["cooperation"]


class RequirementsListView(ListApiView):
    class Meta:
        model = Requirement
        serializer = RequirementItemSerializer
        tags = ["cooperation"]
