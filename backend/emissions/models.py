from django.db import models
from organizations.models import Organization
from sources.models import Source


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=100)

    description = models.TextField()

    quantity = models.FloatField()

    unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    scope = models.CharField(max_length=20)

    record_date = models.DateField()

    is_suspicious = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description