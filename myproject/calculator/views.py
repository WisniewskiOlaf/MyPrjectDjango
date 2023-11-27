from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib

from calculator.models import User

def hello(request, number):
    return HttpResponse(f"Hello{number}")

@csrf_exempt
def calc(request):
    data = json.loads(request.body)
    if data["operation"] == "+":
        result = data['a'] + data['b']
    elif data["operation"] == "*":
        result = data['a'] * data['b']
    return HttpResponse(f"{result}")
    
def get_users(request):
    users = User.objects.all()
    user_data = []
    for user in users:
        user_data.append(user.username)
    return JsonResponse({"Users":user_data})

@csrf_exempt
def add_user(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    users = User.objects.all()
    for existing_user in users:
        if existing_user.username == username:
            return HttpResponse("User already exist",status=400)
    
    user = User(username=username,password=password)
    user.save()
    
    return JsonResponse({"username":user.username,"password":user.password})

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    password = hashlib.sha256(password.encode("utf-8")).hexdigest()
    try:
        user = User.objects.get(username=username,password=password)
        return HttpResponse("user exists!",status=200)
    except:
        return HttpResponse("user dose not exist!",status=400)
    