from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    address = models.TextField()
    net_worth = models.IntegerField(default=0)
