from django.urls import path

from moloko_backend.bids.views import (
    CooperationBidCreateView,
    LogisticBidCreateView,
)

urlpatterns = [
    path("logistic.create", LogisticBidCreateView.as_view()),
    path("cooperation.create", CooperationBidCreateView.as_view()),
]
