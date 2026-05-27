from audits.models import AuditLog
from rest_framework.generics import ListAPIView

import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmissionRecord
from .serializers import EmissionRecordSerializer

from organizations.models import Organization
from sources.models import Source


class UploadCSVView(APIView):

    def post(self, request):

        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        df = pd.read_csv(file)

        organization = Organization.objects.first()
        if not organization:
             organization = Organization.objects.create(
             name="Default Organization"
             )
        source = Source.objects.create(
            organization=organization,
            source_type="SAP",
            file_name=file.name
        )

        records_created = []

        for _, row in df.iterrows():

            suspicious = False

        if float(row["quantity"]) < 0:
            suspicious = True

        record = EmissionRecord.objects.create(
            organization=organization,
            source=source,
            category=str(row.get("category", "")),
            description=str(row.get("description", "")),
            quantity=float(row.get("quantity", 0)),
            unit=str(row.get("unit", "")),
            normalized_unit=str(row.get("unit", "")).lower(),
            scope=str(row.get("scope", "")),
            record_date=row.get("record_date"),
            is_suspicious=suspicious
        )

        records_created.append(record)

        serializer = EmissionRecordSerializer(
            records_created,
            many=True
        )

        return Response(serializer.data)
    
class ReviewEmissionView(APIView):

    def patch(self, request, pk):

        try:
            record = EmissionRecord.objects.get(id=pk)

        except EmissionRecord.DoesNotExist:
            return Response(
                {"error": "Record not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        action = request.data.get("action")

        if action == "approve":

            record.status = "APPROVED"

            audit_action = "APPROVED"

        elif action == "reject":

            record.status = "REJECTED"

            audit_action = "REJECTED"

        else:
            return Response(
                {"error": "Invalid action"}
            )

        record.save()

        AuditLog.objects.create(
            emission_record=record,
            action=audit_action,
            performed_by="admin",
            notes=f"Record {action}d by analyst"
        )

        return Response({
            "message": f"Record {action}d successfully"
        })
    
class EmissionRecordListView(ListAPIView):

    queryset = EmissionRecord.objects.all().order_by("-id")

    serializer_class = EmissionRecordSerializer