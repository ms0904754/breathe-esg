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

        try:
            df = pd.read_csv(file)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

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

            try:

                suspicious = False

                quantity = float(row["quantity"])

                if quantity < 0:
                    suspicious = True

                record = EmissionRecord.objects.create(
                    organization=organization,
                    source=source,
                    category=str(row["category"]),
                    description=str(row["description"]),
                    quantity=quantity,
                    unit=str(row["unit"]),
                    normalized_unit=str(row["unit"]).lower(),
                    scope=str(row["scope"]),
                    record_date=str(row["record_date"]),
                    is_suspicious=suspicious
                )

                records_created.append(record)

            except Exception as e:

                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = EmissionRecordSerializer(
            records_created,
            many=True
        )

        return Response(serializer.data)