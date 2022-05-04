from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    DateOfBirth = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    ResidentialAddress = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=20)

# Create your models here.
