from django.db import models
from django.contrib.auth.models import AbstractUser

class Leads(models.Model):
    
    class Meta:
        verbose_name = 'Leads'
        verbose_name_plural = 'My Leads'

