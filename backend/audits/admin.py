from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "action",
        "emission_record",
        "performed_by",
        "timestamp",
    )

    search_fields = (
        "action",
        "performed_by",
        "notes",
    )

    list_filter = (
        "action",
        "timestamp",
    )

    readonly_fields = (
        "timestamp",
    )