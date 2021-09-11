
from rest_framework import serializers
from employee1.models import Employee

class EmployeeSerialize(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('id','Ecode','Name','Address','Pincode','Mobile','Salary','Username','Password')