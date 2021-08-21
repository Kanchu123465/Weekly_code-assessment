from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from faculty.serialize import FacultySerialize
from faculty.models import Faculty


def Addfaculty(request):
    return render(request,'faculty.html')
def facultylogin(request):
    return render(request,'login.html')

@csrf_exempt
def Facultyadd(request):
    if(request.method=="POST"):
            mydata=JSONParser().parse(request)
            faculty_serialize=FacultySerialize(data=mydata)
            if (faculty_serialize.is_valid()):
                faculty_serialize.save()
                return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def Viewallfaculty(request):
    if (request.method=="GET"):
        faculty=Faculty.objects.all()
        faculty_serialize=FacultySerialize(faculty,many=True)
        return JsonResponse(faculty_serialize.data,safe=False)

@csrf_exempt
def Faculty_details(request,fetchid):
    try:
        faculty=Faculty.objects.get(id=fetchid)
    except Faculty.DoesNotExist:
        return HttpResponse("Invalid faculty Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        faculty_serializer=FacultySerialize(faculty)
        return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        faculty.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         faculty_serialize=FacultySerialize(faculty,data=mydata)
         if (faculty_serialize.is_valid()):
             faculty_serialize.save()
             return JsonResponse(faculty_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(faculty_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def FacultySearch(request,fcode):
    try:
        faculty=Faculty.objects.get(Fcode=fcode)
    except Faculty.DoesNotExist:
        return HttpResponse("faculty not found",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        faculty_serializer=FacultySerialize(faculty)
        return JsonResponse(faculty_serializer.data,safe=False,status=status.HTTP_200_OK)

