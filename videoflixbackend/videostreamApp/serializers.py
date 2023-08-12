from rest_framework.serializers import ModelSerializer
from .models import Video,MyUser
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model=MyUser
        fields=['id','email']

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        instance.set_password(password)
        instance.save()
        return instance

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id','file','title','description','created_at','file_480','file_720','file_1000']