from rest_framework.serializers import ModelSerializer
from .models import Video
from rest_framework import serializers



class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ['file','title','description','created_at']