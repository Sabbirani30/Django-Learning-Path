from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    Student_ID = models.IntegerField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Age = models.IntegerField()
    Department = models.CharField(max_length=100)