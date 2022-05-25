import phonenumbers
from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# create User here
class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    work_phone = models.IntegerField()


