from django.contrib import admin

from moloko_backend.cooperation.models import TermOfCooperation, Partner, Requirement


@admin.register(TermOfCooperation)
class TermsAdmin(admin.ModelAdmin):
    list_filter = ("type",)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    pass
