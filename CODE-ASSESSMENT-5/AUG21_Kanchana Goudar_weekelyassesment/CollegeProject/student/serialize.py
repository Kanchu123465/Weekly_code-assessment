from rest_framework import serializers
from student.models import Student

class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('Name','Admo','Rollno','College','Parentname')