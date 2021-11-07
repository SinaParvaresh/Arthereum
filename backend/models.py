from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    address = models.TextField()
    net_worth = models.IntegerField(default=0)

class Auction(models.Model):
    name = models.TextField()
    cur_bid = models.IntegerField(default=10)
    highest = models.IntegerField(default=11)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
