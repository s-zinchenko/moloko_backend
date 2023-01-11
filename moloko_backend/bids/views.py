from django_serializer.v2.serializer import Serializer
from django_serializer.v2.views import CreateApiView

from moloko_backend.bids.forms import LogisticBidCreateForm, CooperationBidCreateForm
from moloko_backend.bids.models import LogisticBid, CooperationBid


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
