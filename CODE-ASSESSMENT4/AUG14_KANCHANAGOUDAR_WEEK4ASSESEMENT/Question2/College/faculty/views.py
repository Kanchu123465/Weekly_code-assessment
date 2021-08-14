from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def Myaddpage2(request):
    if(request.method=="POST"):
        getName=request.POST.get("fname")
        getadr=request.POST.get("adress")
        getdep=request.POST.get("department")
        getcg=request.POST.get("fcollege")
        
        
        mydict={"fname":getName,"adress":getadr,"department":getdep,"fcollege":getcg}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed")
