from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
import unittest
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
import json

# Create your tests here.

class RegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
       
        self.data = {"email": "testuser@mail.de","password":"testpassword"}  # Als JSON-kodierte Zeichenkette
        
        self.user = User.objects.create_user(username='testuser', password='testpass')
       
        self.token = Token.objects.create(user=self.user)
      
       
       
        
    def test_registration(self):
         self.client=Client()
         
         response=self.client.post('/register/',self.data)
         self.assertEqual(response.status_code, 200)

class LoginTest(TestCase):
    def test_login(self):
        self.client=Client()
        self.user=User.objects.create(username='test_user',password='test_user')
        self.client.login(username='test_user',password='test_user')
        response=HttpResponse()
        self.assertEqual(response.status_code, 200)


