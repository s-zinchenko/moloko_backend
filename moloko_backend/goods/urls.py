from django.urls import path

from moloko_backend.goods.views import ProductsListView

urlpatterns = [
    path("list", ProductsListView.as_view())
]