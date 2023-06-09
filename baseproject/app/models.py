from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class products(models.Model):
    name = models.CharField(max_length=150)
    discription = models.TextField(max_length=1000)
    price = models.IntegerField()
