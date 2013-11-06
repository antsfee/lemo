import sys , os
from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from serializers import UserSerializer
from Apple.views import index , UserList 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
                       
    # Examples:
    # url(r'^$', 'lemon.views.home', name='home'),
    # url(r'^lemon/', include('lemon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    # Uncomment the next two lines to enable the admin:
    # from django.contrib import admin
    # admin.autodiscover()
    
    #url(r'^/$','index'),
    url(r'^user/', UserList.as_view()),
  
    url(r'^$',index),
 
)

urlpatterns = format_suffix_patterns(urlpatterns)
