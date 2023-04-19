from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Article
        fields= "__all__"
        
        # fields= ['author,title,slug,content,publish,created,updated,status,'] 
        # exclude=('created','')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= "__all__"  