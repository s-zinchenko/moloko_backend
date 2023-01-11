from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from moloko_backend.bids.models import LogisticBid, CooperationBid


class LogisticBidResource(resources.ModelResource):
    class Meta:
        model = LogisticBid


class CooperationBidResource(resources.ModelResource):
    class Meta:
        model = CooperationBid


@admin.register(LogisticBid)
class LogisticBidAdmin(ImportExportModelAdmin):
    resource_classes = [LogisticBidResource]


@admin.register(CooperationBid)
class CooperationBidAdmin(ImportExportModelAdmin):
    resource_classes = [CooperationBidResource]
