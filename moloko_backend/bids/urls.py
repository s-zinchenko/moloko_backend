from django.urls import path

from moloko_backend.bids.views import (
    CooperationBidCreateView,
    LogisticBidCreateView,
    PriceListBidCreateView,
)

urlpatterns = [
    path("logistic.create", LogisticBidCreateView.as_view()),
    path("cooperation.create", CooperationBidCreateView.as_view()),
    path("price_list.create", PriceListBidCreateView.as_view()),
]
