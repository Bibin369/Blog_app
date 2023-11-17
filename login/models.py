from django.db import models

# Create your models here.

class registeration(models.Model):
    name=models.CharField(default="",max_length=100)
    image=models.CharField(default="",max_length=10000)
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)
