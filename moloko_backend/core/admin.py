from django.contrib import admin
from solo.admin import SingletonModelAdmin

from moloko_backend.core.models import Company, Fact, Agreement


class FactInline(admin.TabularInline):
    model = Fact


@admin.register(Company)
class CompanyAdmin(SingletonModelAdmin):
    inlines = [
        FactInline,
    ]


@admin.register(Agreement)
class AgreementAdmin(SingletonModelAdmin):
    pass
