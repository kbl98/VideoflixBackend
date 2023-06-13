from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.contrib.auth import authenticate

# Create your views here.
class UserRegistrationView(APIView):
    """
    Funtion to registrate a new User to the Kanbanboard by posting email, username and password 
    Test if user is already registrated.
    """
    def post(self, request):
        data=request.data
        email=data['email']
        username=data['email']
    
        if not self.username_exists(username,email):
            user=User.objects.create_user(username=data['email'],email=data['email'],password=data['password'])
            user.is_staff = True
            user.save()
            return JsonResponse({'Message':'User created'})
           
        return JsonResponse({'Message':'User already exists'})

    def username_exists(self,username,email):
        if User.objects.filter(username=username).exists():
            return True
        if User.objects.filter(email=email).exists():
            return True
        return False   