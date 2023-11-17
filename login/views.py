import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from login.serializer import registerSerializer
from login.models import registeration
from django.db.models import Q
# Create your views here.

@csrf_exempt    
def Register(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=registerSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Registration success"}))
        else:
             return HttpResponse(json.dumps({"status":"Registration failed"}))

