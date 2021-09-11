from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib.auth import logout
import json
from employee1.models import Employee
from employee1.serialize import EmployeeSerialize

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def Viewallemployee(request):
    fetchdata=requests.get("http://127.0.0.1:8000/employee/viewallapi/").json()
    return render(request,'views.html',{"data":fetchdata})

def Updateemployee(request):
    return render(request,'update.html')

@csrf_exempt
def employeeadd(request):
    if (request.method=="POST"):
        emp_s=EmployeeSerialize(data=request.POST)
        if(emp_s.is_valid()):
            emp_s.save()
            return JsonResponse(emp_s.data)
            # return redirect(Viewalllibrarian)
        else:
            return HttpResponse("Error in serialization")
    else:
        return HttpResponse("No get method is allowed")

def employeeviewall(request):
    if (request.method=="GET"):
        emps=Employee.objects.all()
        emp_serialize=EmployeeSerialize(emps,many=True)
        return JsonResponse(emp_serialize.data,safe=False)


@csrf_exempt
def employeeview(request,fetchid):
    try:
        emps=Employee.objects.get(id=fetchid)
        
        if (request.method=="GET"):
            emp_serializer=EmployeeSerialize(emps)
            return JsonResponse(emp_serializer.data,status=status.HTTP_200_OK)
        if (request.method=="DELETE"):
            emps.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if (request.method=="PUT"):
            mydata=JSONParser().parse(request)
            emp_serialize=EmployeeSerialize(emps,data=mydata)
            if (emp_serialize.is_valid()):
                emp_serialize.save()
                return JsonResponse(emp_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(emp_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return HttpResponse("Invalid Employee Id",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_searchapi(request):
    try:
        # getUsername = request.POST.get("username")
        # getPassword = request.POST.get("password")
        # getUsers =Employee.objects.filter(Username=getUsername,Password=getPassword)
        # user_serialiser = EmployeeSerialize(getUsers, many=True)
        getecode=request.POST.get("newid")
        getpat=Employee.objects.filter(id=getecode)
        emp_s=EmployeeSerialize(getpat,many=True)
        return render(request,"update.html",{"data":emp_s.data})
       
    except Employee.DoesNotExist:
        return HttpResponse("Invalid employee",status=status.HTTP_404_NOT_FOUND)
    # except:
    #     return HttpResponse("Something went wrong")

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")
    print(getId)
    getlcode=request.POST.get("newEcode")
    print(getlcode)
    getname=request.POST.get("newName")
    print(getname)
    getadress=request.POST.get("newAddress")
    print(getadress)
    getsalary=request.POST.get("newSalary")
    print(getsalary)
    getphone=request.POST.get("newMobile")
    print(getphone)
    getpincode=request.POST.get("newPincode")
    print(getpincode)
    getUsername=request.POST.get("newUsername")
    getPassword=request.POST.get("newPassword")
    mydata={"Ecode":getlcode,"Name":getname,"Address":getadress,"Pincode":getpincode,"Mobile":getphone,"Salary":getsalary,"Username":getUsername,"Password":getPassword}
    jsondata=json.dumps(mydata)
    print(jsondata)
    ApiLink="http://127.0.0.1:8000/employee/viewapi/"+ getId
    requests.put(ApiLink,data=jsondata)
    return redirect(Viewallemployee)


@csrf_exempt
def login_check(request):
    try:
        getUsername = request.POST.get("username")
        getPassword = request.POST.get("password")
        getUsers =Employee.objects.filter(Username=getUsername, Password=getPassword)
        user_serialiser = EmployeeSerialize(getUsers, many=True)
        print(user_serialiser.data)
        if (user_serialiser.data):
            for i in user_serialiser.data:
                getId = i["id"]
                getName = i["Username"]
                

            # Session set 
            request.session['uid'] = getId
            request.session['uname'] = getName
            #Session 
                 
           
            return render(request,'views.html',{"data":user_serialiser.data})    

        else:
            return HttpResponse("Invalid Credentials")        
            
            
    except Employee.DoesNotExist:
        return HttpResponse("Invalid Username or Password ", status=status.HTTP_404_NOT_FOUND)


def logout_user(request):
    logout(request)
    template='login.html'
    return render(request,template)
