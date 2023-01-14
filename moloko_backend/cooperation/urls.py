from django.urls import path

from moloko_backend.cooperation.views import (
    TermsListView,
    PartnersListView,
    RequirementsListView,
)

urlpatterns = [
    path("terms", TermsListView.as_view()),
    path("partners.list", PartnersListView.as_view()),
    path("requirements.list", RequirementsListView.as_view()),
]
