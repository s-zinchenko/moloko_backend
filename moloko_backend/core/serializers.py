from typing import Optional, Any

from django_serializer.v2.serializer import ModelSerializer, Serializer
from marshmallow import fields, pre_dump

from moloko_backend.core.models import Company, Fact, Agreement


class FactSerializer(ModelSerializer):
    class SMeta:
        model = Fact
        fields = (
            "number",
            "title",
        )


class AboutCompanySerializer(ModelSerializer):
    class SMeta:
        model = Company
        fields = (
            "name",
            "description",
            "map_image",
        )

    facts = fields.Nested(FactSerializer, many=True)

    @pre_dump
    def prepare(self, obj: Company, **kwargs: Optional[Any]) -> Company:
        obj.facts = obj.fact_set.all()
        obj.map_image = obj.map_image.url
        return obj


class GetAgreementSerializer(ModelSerializer):
    class SMeta:
        model = Agreement
        fields = (
            "file",
        )

    @pre_dump
    def prepare(self, obj: Agreement, **kwargs: Optional[Any]) -> Agreement:
        obj.file = obj.file.url
        return obj
