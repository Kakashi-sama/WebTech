from django.db import models

# Create your models here.
 
class Menu(models.Model):
        item    = models.CharField(max_length=120, primary_key=True)
        price   = models.CharField(max_length=120, null=False)
        address = models.CharField(max_length=120, null=False)