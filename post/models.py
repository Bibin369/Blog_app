from django.db import models

# Create your models here.

class postmodel(models.Model):
    userid=models.CharField(default="",max_length=100)
    title=models.CharField(default="",max_length=1000)
    message=models.CharField(default="",max_length=1000)
