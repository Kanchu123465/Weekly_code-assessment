from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def Myaddpage(request):
    if(request.method=="POST"):
        getName=request.POST.get("name")
        getadm=request.POST.get("admission")
        getroll=request.POST.get("roll")
        getcg=request.POST.get("college")
        getpa=request.POST.get("parentname")
        
        mydict={"name":getName,"admission":getadm,"roll":getroll,"college":getcg,"parentname":getpa}
        result=json.dumps(mydict)
        return HttpResponse(result)
    else:
        return HttpResponse("No get method is allowed")

