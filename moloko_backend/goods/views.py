from django_serializer.v2.views import ListApiView

from moloko_backend.goods.models import Category
from moloko_backend.goods.serializers import CategorySerializer


class ProductsListView(ListApiView):
    class Meta:
        model = Category
        tags = ["catalog"]
        serializer = CategorySerializer

    def get_queryset(self):
        return Category.objects.prefetch_related("product_set").all()
