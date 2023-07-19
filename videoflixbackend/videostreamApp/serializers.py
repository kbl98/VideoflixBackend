from rest_framework.serializers import ModelSerializer
from .models import Video
from rest_framework import serializers



class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['id','file','title','description','created_at','file_480','file_720','file_1000']