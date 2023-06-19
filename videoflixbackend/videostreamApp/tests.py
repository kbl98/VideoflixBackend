from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import unittest
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import MyUser
import json

# Create your tests here.

class RegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
       
        self.data = {"email": "testuser@mail.de","password":"testpassword"}  # Als JSON-kodierte Zeichenkette
        
        self.user = MyUser.objects.create_user(email='testuser@test.de', password='testpass')
       
        self.token = Token.objects.create(user=self.user)
        self.user.verification_code='743736'
        self.verification_url='/verify/?code=743736'
      
       
       
        
    def test_registration(self):
         self.client=Client()
         
         response=self.client.post('/register/',self.data)
         self.assertEqual(response.status_code, 200)
       

    def test_verification(self):
        verification_code = '743736'
        verification_url = '/verify/'
        response=self.client.get(verification_url,params={'code': verification_code})
        self.assertEqual(response.status_code,200)

class LoginTest(TestCase):
    

    def test_loginVerified(self):
        self.client=Client()
        data={"email":'test_user@test.de',"password":'test_user'}
        self.user=MyUser.objects.create_user(email='test_user@test.de',password='test_user')
        self.user.is_verified=True
        self.user.save()
        response=self.client.post('/login/',data)
        self.assertEqual(response.status_code, 200)

class LoginUnverfiedTest(TestCase):
    def test_loginUnverified(self):
        self.client=Client()
        data={"email":'test_user2@test.de',"password":'test_user'}
        self.user=MyUser.objects.create_user(email='test_user2@test.de',password='test_user')
        response=self.client.post('/login/',data, follow=False)
        self.assertEqual(response.status_code, 401)


