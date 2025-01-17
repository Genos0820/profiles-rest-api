from django.shortcuts import render # type: ignore
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """Test APIView"""
    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped maually to URLs',
        ]
        
        return Response({"message":"Hello","an_apiview":an_apiview})


