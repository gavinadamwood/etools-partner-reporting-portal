from django.conf.urls import url

from .views import (
    ProgrammeDocumentAPIView,
    ProgrammeDocumentDetailsAPIView,
    ProgrammeDocumentLocationsAPIView,
    ProgressReportPDFView,
    ProgrammeDocumentIndicatorsAPIView,
    ProgressReportAPIView,
    ProgressReportIndicatorsAPIView,
    ProgressReportDetailsAPIView,
    ProgressReportSubmitAPIView,
    ProgressReportReviewAPIView,
    ProgressReportLocationsAPIView,
    ProgrammeDocumentCalculationMethodsAPIView,
    ProgrammeDocumentProgressAPIView
)


urlpatterns = [
    url(r'^(?P<workspace_id>\d+)/programme-document/$',
        ProgrammeDocumentAPIView.as_view(),
        name="programme-document"),
    url(r'^(?P<workspace_id>\d+)/programme-document/(?P<pd_id>\d+)/$',
        ProgrammeDocumentDetailsAPIView.as_view(),
        name="programme-document-details"),
    url(r'^(?P<workspace_id>\d+)/programme-document/(?P<pd_id>\d+)/progress/$',
        ProgrammeDocumentProgressAPIView.as_view(),
        name="programme-document-progress"),
    url(r'^(?P<workspace_id>\d+)/programme-document/(?P<pd_id>\d+)/calculation-methods/$',
        ProgrammeDocumentCalculationMethodsAPIView.as_view(),
        name="programme-document-calculation-methods"),

    url(r'^(?P<workspace_id>\d+)/programme-document/locations/$',
        ProgrammeDocumentLocationsAPIView.as_view(),
        name="programme-document-locations"),
    url(r'^(?P<workspace_id>\d+)/programme-document/indicators/$',
        ProgrammeDocumentIndicatorsAPIView.as_view(),
        name="programme-document-indicators"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/$',
        ProgressReportAPIView.as_view(),
        name="progress-reports"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/(?P<pk>\d+)/$',
        ProgressReportDetailsAPIView.as_view(),
        name="progress-reports-details"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/(?P<pk>\d+)/annex-C-export-PDF/$',
        ProgressReportPDFView.as_view(),
            name="progress-reports-pdf"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/(?P<pk>\d+)/submit/$',
        ProgressReportSubmitAPIView.as_view(),
        name="progress-reports-submit"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/(?P<pk>\d+)/review/$',
        ProgressReportReviewAPIView.as_view(),
        name="progress-reports-review"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/(?P<progress_report_id>\d+)/indicator-reports/$',
        ProgressReportIndicatorsAPIView.as_view(),
        name="progress-reports-indicators"),
    url(r'^(?P<workspace_id>\d+)/progress-reports/(?P<progress_report_id>\d+)/locations/$',
        ProgressReportLocationsAPIView.as_view(),
        name="progress-reports-locations"),
]
