from typing import Optional, Any

from django_serializer.v2.serializer import ModelSerializer, Serializer
from marshmallow import fields, pre_dump

from moloko_backend.core.models import Company, Fact, Management


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


class ManagementPersonSerializer(ModelSerializer):
    class SMeta:
        model = Management
        fields = (
            "role",
            "portrait",
        )

    name = fields.Str()

    @pre_dump
    def prepare(self, obj: Management, **kwargs: Optional[Any]) -> Management:
        obj.portrait = obj.portrait.url
        return obj


class ManagementListSerializer(Serializer):
    management = fields.Nested(ManagementPersonSerializer, many=True)
