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
from rest_framework.renderers import JSONPRenderer
from rest_framework.parsers import JSONParser
import json

class JsonResponse(HttpResponse):
    ''' generate a json format response  '''
    def __init__(self,content={},mimetype=None,status=None,content_type=None):
        if not content_type:
            content_type='application/json'
        
        super(JsonResponse,self).__init__(json.dumps(content),mimetype=mimetype,status=status,content_type=content_type)
        


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
    
    def get(self,request,format='json'):
        
        print 'current data of request ',request.DATA
        
        serialize = UserSerializer(data=request.DATA)
        
        
        
        return render_to_response('index.html')
        
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
        
class UserDetail(APIView):
    
    
    #Retrieve , update or delete a  user    
    
    
    
    def get_object(self,pk):
        
        try:
            
            return User.objects.get(pk=pk)

        
        except User.DoesNotExist:
            
            raise Http404
    
     # Retrieve a  user is make action login return statue (error , success or mistake )
    
    def get(self,request,format='JSON'):
        
        print 'current data is :  ',request.DATA.userName
        return render_to_response('index.html')
            
    
    
    # update the info about the user
        
    def put(self,request,pk,format):
        print 'current data is put :  ',request.DATA.userName
        return render_to_response('index.html')
        
    
    
    # admin delete the user 
    #def delete(self,request,pk,format):
        #sssss
        
########################################################################
class UserLogin(APIView):
    
    
    """ user login handler """    
    
    def post(self,request,format='json'):
        
        #print request.DATA
        
        loginData=UserSerializer(request.DATA).data
        
        #print 'current loginData value is: ',loginData 
        
        #print 'current loginData length :  ',len(loginData)
        try:
        
            obj=User.objects.get(userName__exact=loginData['userName'])
            
        
        except:
            
            return JsonResponse(content={'loginName':'null'}, status=200, 
                               )
        
        actionStatue = {}
        
        print 'post method get userName item:  ',request.POST['userName']
        
        if loginData['passWord'] is None:
            
            ''' passWord is None mean to check userName only is not form submit '''
            
            if obj.userName == loginData['userName']:
                
            
                actionStatue['loginName'] = True
            
            
                return JsonResponse(content=actionStatue,status=200)
            
            else:
                
                return JsonResponse(content=actionStatue,status=200)
                
        
        else:
            
            ''' login form submit  check login data '''
        
            if obj.userName == loginData['userName']:
            
                """ make sure username is valid  """
            
                actionStatue['loginName'] = True
            
            
                if obj.passWord == loginData['passWord']:
                
                    ''' make sure  password is valid'''
                
                    actionStatue['loginPass'] = True
                            
                    #loginStaute = JSONPRenderer().render(actionStatue)
                    
                    print 'current user id is ', obj.id 
                
                    request.session['user_id'] = obj.id
                            
                    return JsonResponse(actionStatue,status=200)
                                        
                
                else:
                
                    '''   '''
                
                    actionStatue['loginPass'] = False
                            
                    #loginStaute = JSONPRenderer().render(actionStatue)
                            
                    return JsonResponse(actionStatue,status=200)
                
            else:
                ''' name is not  '''
                
                actionStatue['loginName'] = False
                return JsonResponse(content=actionStatue,status=200)





########################################################################
class Users(APIView):
    
    """ a common handler for user action """     
    
    
    #----------------------------------------------------------------------
    def  login(self):
        
        """  """
        
        
    
    
                
                 
            
            
            
            
        
        
        
        
    
        
    
    