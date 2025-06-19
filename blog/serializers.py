from rest_framework import serializers
from .models import Blog,Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['title','body','date','author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['post','author','content','date']
        