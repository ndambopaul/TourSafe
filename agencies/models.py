from django.db import models

from core.models import AbstractBaseModel

# Create your models here.


class County(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ServiceCategory(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Agency(AbstractBaseModel):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    service_category = models.ForeignKey(
        ServiceCategory, on_delete=models.SET_NULL, null=True
    )
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)

    def __str__(self):
        return self.name


class Destination(AbstractBaseModel):
    name = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class ServiceProvider(AbstractBaseModel):
    tra_number = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    county = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    service_category = models.CharField(max_length=255, null=True)
