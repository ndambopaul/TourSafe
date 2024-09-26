from django.contrib import admin
from agencies.models import (
    Agency,
    ServiceCategory,
    County,
    Destination,
    ServiceProvider,
)

# Register your models here.


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tra_number",
        "name",
        "phone_number",
        "town",
        "service_category",
    )
    list_filter = ("county", "region", "service_category")


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "county", "region", "phone_number")
    list_filter = ("county", "region", "service_category")


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "name",
    )


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "name",
    )


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "name", "agency")
