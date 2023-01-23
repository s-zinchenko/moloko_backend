from django.contrib import admin
from solo.admin import SingletonModelAdmin

from moloko_backend.core.models import Company, Fact


class FactInline(admin.TabularInline):
    model = Fact


@admin.register(Company)
class CompanyAdmin(SingletonModelAdmin):
    inlines = [
        FactInline,
    ]
