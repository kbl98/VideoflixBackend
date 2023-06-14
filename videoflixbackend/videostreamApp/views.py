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
        username=data.get('email')
       
        if not username:
            raise ValueError("Der angegebene Benutzername muss festgelegt sein")
        if not self.username_exists(username):
            user=User.objects.create_user(username=data.get('email'),email=data.get('email'),password=data.get('password'))
            user.is_staff = True
            user.save()
            return JsonResponse({'Message':'User created'})
           
        return JsonResponse({'Message':'User already exists'})

    def username_exists(self,username):
        if User.objects.filter(username=username).exists():
            return True
        return False 


class loginView(ObtainAuthToken):
    """
    View for login of registrated User. Returns token.
    """
    def post(self, request, *args, **kwargs):
        data=request.data
        print(data.get('password'))
        user = authenticate(username=data.get('email'), password=data.get('password'))
        if user is not None:
            user = User.objects.get(email=request.data['email'])
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response({
                'token': token.key,
                'email': user.email,
                'id':user.id,
            })
        else:
            return Response({'message':'Not User'})  