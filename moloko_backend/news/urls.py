from django.urls import path

from moloko_backend.news.views import NewsListView, NewsGetView

urlpatterns = [
    path("list", NewsListView.as_view()),
    path("get", NewsGetView.as_view()),
]
