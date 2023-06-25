from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Location
            fields = '__all__'
            
        
class PurposeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Purpose
            fields = '__all__'