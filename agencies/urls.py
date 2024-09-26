from django.urls import path
from agencies.views import home, agency_details, upload_service_provider, verify_provider

urlpatterns = [
    path("", home, name="home"),
    path("agency-details/<int:id>/", agency_details, name="agency-details"),
    path("upload-providers/", upload_service_provider, name="upload-providers"),
    path("verify-provider/", verify_provider, name="verify-provider"),
]
