from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollNumber = models.IntegerField()
    marks = models.IntegerField()
    phoneNumber = models.CharField(max_length=15)
