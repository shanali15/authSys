from django.http import JsonResponse
from django.http import HttpResponse
import json
from .models import Users
from django.contrib import messages
import bcrypt
import jwt
import time

global mySalt
mySalt = b'$2b$12$fTurMmEVmQg7QcxG6q2Hde' #mySalt = bcrypt.gensalt()
def user_signup(request):
    body = request.body
    loadedJson = json.loads(body)
    email = loadedJson['email']
    password = loadedJson['password']
    username = loadedJson['username']
    bytePwd =  password.encode('utf-8')  
    hash = bcrypt.hashpw(bytePwd, mySalt)
    myuser = Users.objects.create(email= "shanali15f@gmail.com",password= hash,username= "shanali15f")
    messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

    return HttpResponse("SignUp SuccessFull")

def user_login(request):
    t = time.time()
    body = request.body
    loadedJson = json.loads(body)
    email = loadedJson['email']
    password = loadedJson['password']
    bytePwd =  password.encode('utf-8')  
    hash = bcrypt.hashpw(bytePwd, mySalt)
    user = Users.objects.filter(email=email,password=hash).values()
    # user = Users.objects.filter(email="shanali15f@gmail.com")
    length = len(user)
    if(user[0]['token']==''):
        newtoken = jwt.encode(
            {password:password},
            mySalt,
            algorithm='HS256'
        )
        Users.objects.filter(email=email,password=hash).update(token=newtoken).values()
        print(user)
    user = Users.objects.filter(email=email,password=hash).values()    
    if (length == 1):
        timetaken = t-time.time()
        return JsonResponse({
            "status":True,
            "message": "successfull",
            "token" : user[0]['token'],
            "timetaken": timetaken
        })
    else:
        return HttpResponse("Login Failed")
        
def check_token(request):
#     # print(request.headers.get('Authorization'))
#     # print((request.headers['authorization']))
    return HttpResponse("wokring")
#     return
