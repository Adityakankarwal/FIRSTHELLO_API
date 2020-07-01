from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
# Create your views here.

class ApiviewHello(APIView):
    """TEst the API view"""
    serializer_class = serializers.HelloSeralizer
    def get(self, request, format=None):
        """Return List of API View Feature"""
        lst = ["use HppMethod as function(get, post, patch, push, delete)",
               "API view is similare to DJANGO VIEW",
               "Give most control over the logic",
               "Is mapped manually to URLs"
               ]
        return Response({"message":"Hello from API View", "list of API":lst})

    def post(self, request):
        """Create Hello Name with message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handel updating object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handel a Partially updating object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})