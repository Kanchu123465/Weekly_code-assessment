from django.db import models

# Create your models here.
class Employee(models.Model):
    Ecode=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=50)
    Salary=models.CharField(max_length=50)
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
