from rest_framework import serializers
from faculty.models import Faculty

class FacultySerialize(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('Fcode','Name','Department','Address','Mobileno','Username','Password')