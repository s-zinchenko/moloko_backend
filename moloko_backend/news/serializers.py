from django_serializer.v2.serializer import Serializer, ModelSerializer
from marshmallow import fields

from moloko_backend.news.models import News


class NewsItemSerializer(ModelSerializer):
    class SMeta:
        model = News
        fields = (
            "title",
            "body",
            "date",
        )


class NewsListSerializer(Serializer):
    news = fields.Nested(NewsItemSerializer, many=True)
