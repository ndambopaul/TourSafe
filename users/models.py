from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import AbstractBaseModel

# Create your models here.

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class User(AbstractUser, AbstractBaseModel):
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
