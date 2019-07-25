from django.db import models

# Create your models here.
class account(models.Model):
    username    = models.CharField(max_length=120, primary_key=True)
    email       = models.CharField(max_length=255, null=False)
    password    = models.CharField(max_length=200, null=False)
    phonenumber = models.CharField(max_length=10, null=True)