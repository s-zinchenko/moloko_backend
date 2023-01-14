from typing import Any, Optional

from django_serializer.v2.serializer import ModelSerializer, Serializer
from marshmallow import fields, pre_dump

from moloko_backend.cooperation.models import (
    TermOfCooperation,
    Partner,
    Requirement,
)


class TermsItemSerializer(ModelSerializer):
    class SMeta:
        model = TermOfCooperation
        fields = ("term",)


class PartnerItemSerializer(ModelSerializer):
    class SMeta:
        model = Partner
        fields = ("logo",)

    @pre_dump
    def prepare(self, obj: Partner, **kwargs: Optional[Any]) -> Partner:
        obj.logo = obj.logo.url
        return obj


class RequirementItemSerializer(ModelSerializer):
    class SMeta:
        model = Requirement
        fields = ("title",)


class TermsListSerializer(Serializer):
    terms = fields.Nested(TermsItemSerializer, many=True)


class PartnerListSerializer(Serializer):
    partners = fields.Nested(PartnerItemSerializer, many=True)


class RequirementsListSerializer(Serializer):
    requirements = fields.Nested(RequirementItemSerializer, many=True)
