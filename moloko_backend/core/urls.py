from django.urls import path
from moloko_backend.core.views import AboutCompanyView, ManagementListView

urlpatterns = [
    path("about", AboutCompanyView.as_view()),
    path("management.list", ManagementListView.as_view()),
]
