from django_serializer.v2.views import GetApiView, ListApiView

from moloko_backend.news.models import News
from moloko_backend.news.serializers import NewsItemSerializer, NewsListSerializer


class NewsListView(ListApiView):
    class Meta:
        model = News
        serializer = NewsListSerializer
        tags = ["news"]

    def execute(self, request, *args, **kwargs):
        qs = super().execute(request, *args, **kwargs)
        return {"news": qs}


class NewsGetView(GetApiView):
    class Meta:
        model = News
        serializer = NewsItemSerializer
        tags = ["news"]
