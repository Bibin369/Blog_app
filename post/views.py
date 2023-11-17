import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from post.serializer import postSerializer
from post.models import postmodel
from django.db.models import Q
# Create your views here.

@csrf_exempt    
def Post(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        serializer_check=postSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"Registration success"}))
        else:
             return HttpResponse(json.dumps({"status":"Registration failed"}))

@csrf_exempt
def ViewAll(request):
    if request.method=="POST":
        postList = postmodel.objects.all()
        serialize_data=postSerializer(postList,many=True)
        return HttpResponse(json.dumps(serialize_data.data))
    
@csrf_exempt    
def Search(request):
    if request.method=="POST":
        received_data=json.loads(request.body)
        getuserid=received_data["userid"]
        data=list(postmodel.objects.filter(Q(userid__icontains=getuserid)).values())
        return HttpResponse(json.dumps(data))
