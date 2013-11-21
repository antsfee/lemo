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
from django.core.context_processors import csrf

def Index(request):
    #print  "xxx"
    #print  'root_path'+settings.ROOT_PATH
    return render_to_response('index.html')
    
##########################################################################

def LoginT(request):
    
    c = {}
    c.update(csrf(request))
    return render_to_response('MLogin.html',c)
    
    
def RegisterT(request):
    
    c = {}
    c.update(csrf(request))
    return render_to_response('register.html',c)    
    
##########################################################################    

#def RegisterT(request):
    

class UserList(APIView):
    
    ''' list all of wines ,or create a new user'''
    
    # get a detail info 
    
    #def get(self,request,format='json'):
        
        
    # register a  new user of website 
        
    def post(self,request,format='json'):
        
        #print "current data of create ",request.DATA
        
        serialize = UserSerializer( data=request.DATA )
        
        print "current data of create ",request.DATA
        
        if serialize.is_valid():
            
            serialize.save()
            
            return Response(data=serialize.data, status=status.HTTP_201_CREATED)
        
        
        else:
            
            return Response(data=serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        
########################################################################
""" class UserDetail(APIView):
    
    
    #Retrieve , update or delete a  user    
    
    
    
    def get_object(self,pk):
        
        try:
            
            return User.objects.get(pk=pk)

        
        except User.DoesNotExist:
            
            raise Http404
    
     # Retrieve a  user is make action login return statue (error , success or mistake )
    
    def get(self,request,pk,format='JSON'):
            
    
    
    # update the info about the user
        
    def put(self,request,pk,format):
        
    
    
    # admin delete the user 
    def delete(self,request,pk,format):
        #sssss
"""
            
            
