from django.db import models

# Create your models here.

class Employee(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=60)
    salary=models.FloatField()
    address=models.CharField(max_length=250)
