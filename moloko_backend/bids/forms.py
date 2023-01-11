from django.forms import ModelForm

from moloko_backend.bids.models import LogisticBid, CooperationBid
from moloko_backend.bids.validators import ValidatePhoneMixin


class LogisticBidCreateForm(ValidatePhoneMixin, ModelForm):
    class Meta:
        model = LogisticBid
        fields = (
            "full_name",
            "departure_address",
            "contact_phone",
            "cargo_weight",
            "email",
            "cargo_descriptions",
        )


class CooperationBidCreateForm(ValidatePhoneMixin, ModelForm):
    class Meta:
        model = CooperationBid
        fields = (
            "full_name",
            "contact_phone",
            "email",
            "company_name",
            "document",
            "comment",
        )
