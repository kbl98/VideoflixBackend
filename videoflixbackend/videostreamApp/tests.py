from django.test import TestCase,override_settings
from django.test import Client
from django.contrib.auth.models import User
import unittest
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import MyUser,Video
from django.core.files.uploadedfile import SimpleUploadedFile
import json
from videostreamApp.singals import send_post_save, send_post_delete
from videostreamApp.singals import export_videos_post_save
from django.db.models import signals

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


class GetVideosTest(TestCase):

    @override_settings(DISABLE_SIGNALS=True)  
    def setUp(self):
        
        self.client=Client()
        file1_content = b'Test file content'
        file1_name = 'test_file.mp4'
        file1 = SimpleUploadedFile(file1_name, file1_content, content_type='video/mp4')
        file2_content = b'Test file content'
        file2_name = 'test_file.mp4'
        file2 = SimpleUploadedFile(file2_name, file2_content, content_type='video/mp4')
        self.user = MyUser.objects.create_user(email='testuser@test.de', password='testpass')
        self.video1 = Video.objects.create(title='Video 1', description='Description 1', file=file1)
        self.video1.save()
        self.video2 = Video.objects.create(title='Video 2', description='Description 2', file=file2)
        self.video2.save()
        self.video2Id=self.video2.id
        #self.token = Token.objects.create(user=self.user)

   
    def test_getVideos(self):
        self.token = Token.objects.create(user=self.user)
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token.key
        response=self.client.get('/videos/')
        self.assertEqual(response.status_code, 200)


    def test_getVideosWithoutToken(self):
        response=self.client.get('/videos/')
        self.assertEqual(response.status_code, 401)

    def test_getExplizitVideo(self):
        self.token = Token.objects.create(user=self.user)
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + self.token.key
        id=self.video2Id
        url='/videos/'+str(id)+'/'
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)

        


