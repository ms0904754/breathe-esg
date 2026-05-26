from django.contrib import admin
from .models import EmissionRecord


@admin.register(EmissionRecord)
class EmissionRecordAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "description",
        "category",
        "quantity",
        "unit",
        "scope",
        "status",
        "is_suspicious",
    )