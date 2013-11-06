# Create your views here.
from Apple.serializers import UserSerializer
from Apple.models import User
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render_to_response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from django.conf import settings


def index(request):
    print  "xxx"
    print  'root_path'+settings.ROOT_PATH
    return render_to_response('index.html')
    
    

class UserList(APIView):
    
    ''' list all of wines ,or create a new user'''
    
    def get(self,request,format='json'):
        
        users = User.objects.all()
        
        serializer = UserSerializer( users )
        
        return Response(data=serializer.data)
        
        
    def post(self,request,format='json'):
        
        serialize = UserSerializer( data=request.DATA )
        
        if serialize.is_valid():
            
            serialize.save()
            
            return Response(data=serialize.data, status=status.HTTP_201_CREATED)
        
        
        else:
            
            return Response(data=serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
########################################################################

class ArticleList(APIView):
    
    """ list all of lemo or create a new article """

    #----------------------------------------------------------------------
    
    def get(self,request,format='json'):
    
        
        
    
    
            
            
