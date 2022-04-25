from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=24,unique=True)
    password = models.CharField(max_length=24)
    username = models.CharField(max_length=24)
    token = models.CharField(max_length=255,null=False)