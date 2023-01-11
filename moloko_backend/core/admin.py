from django.contrib import admin
from solo.admin import SingletonModelAdmin

from moloko_backend.core.models import Company, Fact, Management


class FactInline(admin.TabularInline):
    model = Fact


@admin.register(Company)
class CompanyAdmin(SingletonModelAdmin):
    inlines = [
        FactInline,
    ]


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    fields = (
        "last_name",
        "first_name",
        "middle_name",
        "role",
        "portrait",
    )
