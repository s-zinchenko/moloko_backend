from django.contrib import admin

from moloko_backend.goods.models import Product, Category


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
