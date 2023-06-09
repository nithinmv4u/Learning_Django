from django.db import models

# Create your models here.
class MyModel(models.Model):
    my_field=models.CharField(max_length=100)
    my_num=models.IntegerField(default=0)