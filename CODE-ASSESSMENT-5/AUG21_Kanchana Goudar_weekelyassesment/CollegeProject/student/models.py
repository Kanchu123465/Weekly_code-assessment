from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Admo=models.IntegerField()
    Rollno=models.IntegerField()
    College=models.CharField(max_length=50)
    Parentname=models.CharField(max_length=50)
