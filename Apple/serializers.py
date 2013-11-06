from rest_framework import serializers
from models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('userName', 'passWord', 'gender', 'mail', 'registerTime')
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta():
        model = Album
        fields = ('albumName', 'albumDescription', 'albumCreateTime', 'user')
        
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Photo
        fields = ('photoName', 'photoPath', 'album')
        
class TagSerializer(serializers.ModelSerializer):
    class Meta():
        model = Tag
        fields = ('tagName', 'tagDescription')
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Article
        fields = ('title', 'content', 'tag', 'user')