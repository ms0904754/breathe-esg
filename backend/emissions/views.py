from audits.models import AuditLog
from rest_framework.generics import ListAPIView

import pandas as pd
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmissionRecord
from .serializers import EmissionRecordSerializer

from organizations.models import Organization
from sources.models import Source


class UploadCSVView(APIView):

    REQUIRED_COLUMNS = {
        "description", "category", "quantity",
        "unit", "scope", "record_date"
    }

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
                {"error": f"Could not parse CSV: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ✅ FIX 1: Validate required columns up front
        missing = self.REQUIRED_COLUMNS - set(df.columns.str.strip().str.lower())
        if missing:
            return Response(
                {"error": f"Missing columns: {', '.join(missing)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ✅ FIX 2: Normalize column names (strip whitespace, lowercase)
        df.columns = df.columns.str.strip().str.lower()

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

        for index, row in df.iterrows():
            try:
                quantity = float(row["quantity"])
                suspicious = quantity < 0

                # ✅ FIX 3: Parse record_date properly instead of passing raw string
                try:
                    record_date = pd.to_datetime(row["record_date"]).date()
                except Exception:
                    return Response(
                        {
                            "error": (
                                f"Row {index + 2}: invalid date format "
                                f"'{row['record_date']}'. Expected YYYY-MM-DD."
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                record = EmissionRecord.objects.create(
                    organization=organization,
                    source=source,
                    category=str(row["category"]).strip(),
                    description=str(row["description"]).strip(),
                    quantity=quantity,
                    unit=str(row["unit"]).strip(),
                    normalized_unit=str(row["unit"]).strip().lower(),  # ✅ FIX 4: strip before lower
                    scope=str(row["scope"]).strip(),
                    record_date=record_date,  # ✅ now a proper date object
                    is_suspicious=suspicious
                )

                records_created.append(record)

            except Exception as e:
                # ✅ FIX 5: Include row number in error so you know exactly which row failed
                return Response(
                    {"error": f"Row {index + 2}: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = EmissionRecordSerializer(records_created, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)