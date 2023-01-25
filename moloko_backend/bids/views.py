from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from django_serializer.v2.serializer import Serializer
from django_serializer.v2.views import CreateApiView

from moloko_backend.bids.forms import (
    LogisticBidCreateForm,
    CooperationBidCreateForm, PriceListBidCreateForm,
)
from moloko_backend.bids.models import LogisticBid, CooperationBid, PriceListBid


class LogisticBidCreateView(CreateApiView):
    class Meta:
        model = LogisticBid
        model_form = LogisticBidCreateForm
        serializer = Serializer
        tags = ["bids"]

    def get_request_json(self):  # type: ignore
        if hasattr(self, "_request_json"):
            return getattr(self, "_request_json")
        if "multipart/form-data" in self.request.content_type:
            return self.request.POST


class CooperationBidCreateView(CreateApiView):
    class Meta:
        model = CooperationBid
        model_form = CooperationBidCreateForm
        serializer = Serializer
        tags = ["bids"]

    def get_request_json(self):  # type: ignore
        if hasattr(self, "_request_json"):
            return getattr(self, "_request_json")
        if "multipart/form-data" in self.request.content_type:
            return self.request.POST

    def execute(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Dict[Any, Any]
    ):
        obj = super().execute(request, *args, **kwargs)
        obj.send_email()
        return obj


class PriceListBidCreateView(CreateApiView):
    class Meta:
        model = PriceListBid
        model_form = PriceListBidCreateForm
        serializer = Serializer
        tags = ["bids"]

    def get_request_json(self):  # type: ignore
        if hasattr(self, "_request_json"):
            return getattr(self, "_request_json")
        if "multipart/form-data" in self.request.content_type:
            return self.request.POST

    def execute(
        self,
        request: WSGIRequest,
        *args: Any,
        **kwargs: Dict[Any, Any]
    ):
        obj = super().execute(request, *args, **kwargs)
        obj.send_email()
        return obj
