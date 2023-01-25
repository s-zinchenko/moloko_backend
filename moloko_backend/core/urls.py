from django.urls import path
from moloko_backend.core.views import AboutCompanyView, GetAgreementView

urlpatterns = [
    path("about", AboutCompanyView.as_view()),
    path("agreement", GetAgreementView.as_view()),
]
