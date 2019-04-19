from django.db import models

# Create your models here.
class account(models.Model):
    name        = models.CharField(max_length=120, primary_key=True)
    email       = models.CharField(max_length=255)
    password    = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=10, null=True)
