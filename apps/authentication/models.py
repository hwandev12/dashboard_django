from django.db import models
from django.contrib.auth.models import AbstractUser


# create User here
class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
