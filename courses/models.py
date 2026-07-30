from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    Student_ID = models.IntegerField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Age = models.IntegerField()
    Department = models.CharField(max_length=100)

class Info(models.Model):
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    Age = models.IntegerField()
    course = models.CharField(max_length=100)
    batch = models.IntegerField()
    department = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)
    textarea = models.TextField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)

    