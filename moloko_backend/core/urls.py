from django.urls import path
from moloko_backend.core.views import AboutCompanyView

urlpatterns = [
    path("about", AboutCompanyView.as_view()),
]
