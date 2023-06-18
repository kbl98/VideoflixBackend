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
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from .models import MyUser
import random
from django.urls  import reverse
import smtplib
import ssl
from django.http import HttpResponse


# Create your views here.
class UserRegistrationView(APIView):
    """
    Funtion to registrate a new User to the Kanbanboard by posting email, username and password 
    Test if user is already registrated.
    """
    
    def post(self, request):
        data=request.data
        email=data.get('email')
        
        if not email:
            raise ValueError("Der angegebene Benutzername muss festgelegt sein")
        if not self.username_exists(email):
            verification_code = self.generate_verification_code()
            user=MyUser.objects.create_user(email=data.get('email'),password=data.get('password'), verification_code=verification_code)
            user.is_staff = True
            user.save()
            verification_code = user.verification_code
            verification_link = reverse('email_verification') + f'?code={verification_code}'
            verification_url = self.request.build_absolute_uri(verification_link)
        
            self.send_verification_email(user,verification_url)
            return JsonResponse({'Message':' Mail sent'})
           
        return JsonResponse({'Message':'User already exists'})

    def username_exists(self,email):
        if MyUser.objects.filter(email=email).exists():
            return True
        return False 
    
    def generate_verification_code(self):
        # Code to generate a verification code
        # You can use any method you prefer to generate a unique verification code
        # For simplicity, let's assume it's a random 6-digit code
        return str(random.randint(100000, 999999))
    
    

    def send_verification_email(self, user,verification_url):
        subject = 'Account Verification'
        message = f'Dear {user.email},\n\nPlease click the link below to verify your email address:\n\n{verification_url}'
        from_email = 'devakad8@gmail.com'
        to_email = user.email
       
        send_mail(subject, message, from_email, [to_email])
    
   

class EmailVerificationView(APIView):
    """
    Function to verify the email address using the verification code
    """
    
    def get(self, request):
        verification_code = request.GET.get('code')
        if verification_code:
            try:
            # Find the user with the given verification code
                user = MyUser.objects.get(verification_code=verification_code)
            except MyUser.DoesNotExist:
                return JsonResponse({'Message': 'Invalid verification code'}, status=400)
        
        # Verify the user and update the verification status
            user.is_verified = True
            user.save()
        
            return JsonResponse({'Message': 'Email successfully verified'})
        return JsonResponse({'Message': 'Code Missing'})

class loginView(ObtainAuthToken):
    """
    View for login of registrated User. Returns token.
    """
    def post(self, request, *args, **kwargs):
        data=request.data
        print(data.get('password'))
        
        user = authenticate(email=data.get('email'), password=data.get('password'))
        if user is not None:
            user = MyUser.objects.get(email=request.data['email'])
            if user.is_verified==True:
                token, created = Token.objects.get_or_create(user=user)
                print(token)
                return Response({'token': token.key,'email': user.email,'id':user.id,
            })
            else:
                return HttpResponse(status=401)
        else:
            return Response({'message':'Not User'})  