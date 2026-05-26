from django.urls import path

from .views import (
    UploadCSVView,
    ReviewEmissionView,
    EmissionRecordListView
)

urlpatterns = [
    path(
        "upload/",
        UploadCSVView.as_view()
    ),

    path(
        "review/<int:pk>/",
        ReviewEmissionView.as_view()
    ),

    path(
        "records/",
        EmissionRecordListView.as_view()
    ),
]