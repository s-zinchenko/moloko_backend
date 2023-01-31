from typing import Optional, Any

from django_serializer.v2.serializer import ModelSerializer
from marshmallow import fields, pre_dump

from moloko_backend.goods.models import Product, Category


class ProductSerializer(ModelSerializer):
    class SMeta:
        model = Product
        fields = (
            "title",
        )


class CategorySerializer(ModelSerializer):
    class SMeta:
        model = Category
        fields = (
            "title",
            "icon",
        )

    product_list = fields.Nested(ProductSerializer, many=True)

    @pre_dump
    def prepare(self, obj: Category, **kwargs: Optional[Any]) -> Category:
        obj.product_list = obj.product_set.all()
        obj.icon = obj.icon.url
        return obj
