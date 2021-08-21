from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.parsers import JSONParser
from rest_framework import status
from student.serialize import StudentSerialize
from student.models import Student

def Addstudent(request):
    return render(request,'Add.html')

@csrf_exempt
def Studentadd(request):
    if(request.method=="POST"):
            mydata=JSONParser().parse(request)
            student_s=StudentSerialize(data=mydata)
            if (student_s.is_valid()):
                student_s.save()
                return JsonResponse(student_s.data,status=status.HTTP_200_OK)
            else:
                return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def Viewallstudent(request):
    if (request.method=="GET"):
        students=Student.objects.all()
        student_serialize=StudentSerialize(students,many=True)
        return JsonResponse(student_serialize.data,safe=False)

@csrf_exempt
def Student_details(request,fetchid):
    try:
        students=Student.objects.get(id=fetchid)
    except Student.DoesNotExist:
        return HttpResponse("Invalid student Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        student_serializer=StudentSerialize(students)
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        students.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         student_serialize=StudentSerialize(students,data=mydata)
         if (student_serialize.is_valid()):
             student_serialize.save()
             return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(student_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def StudentSearch(request,admno):
    try:
        students=Student.objects.get(Admo=admno)
    except Student.DoesNotExist:
        return HttpResponse("Student not found",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        student_serializer=StudentSerialize(students)
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)

