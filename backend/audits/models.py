from django.db import models
from emissions.models import EmissionRecord


class AuditLog(models.Model):

    ACTIONS = [
        ("CREATED", "CREATED"),
        ("UPDATED", "UPDATED"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    ]

    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=50,
        choices=ACTIONS
    )

    performed_by = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.action