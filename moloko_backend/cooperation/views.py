from django.shortcuts import render
from django_serializer.v2.views import ListApiView

from moloko_backend.cooperation.forms import TermsListForm
from moloko_backend.cooperation.models import TermOfCooperation, Partner, Requirement
from moloko_backend.cooperation.serializers import TermsListSerializer, PartnerListSerializer, \
    RequirementsListSerializer


class TermsListView(ListApiView):
    class Meta:
        model = TermOfCooperation
        query_form = TermsListForm
        serializer = TermsListSerializer
        tags = ["cooperation"]

    def get_queryset(self):
        return TermOfCooperation.objects.filter(type=self.request_query["type"])


class PartnersListView(ListApiView):
    class Meta:
        model = Partner
        serializer = PartnerListSerializer
        tags = ["cooperation"]


class RequirementsListView(ListApiView):
    class Meta:
        model = Requirement
        serializer = RequirementsListSerializer
        tags = ["cooperation"]
