from django.contrib import admin

from moloko_backend.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
