from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
from . import models
from rest_framework.authentication import TokenAuthentication
from . import permissions
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
        return Response({"message": "Hello from API View", "list of API": lst})

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


class viewsetHello(viewsets.ViewSet):
    """Hello API VIEWSET"""
    serializer_class = serializers.HelloSeralizer

    def list(self, request):
        """Return a Hello message"""
        view_list = ["Uses Action (list,create,retrieve,Update,partially_update)",
                     "Automatically maps the urls using Router",
                     "Provide more functionality with less code",
                     ]
        return Response({"message": "Hello", "view_function_list": view_list})

    def create(self, request):
        """creating 'Hello' message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello{name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handel getting data by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handel update data"""

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handel getting data by its ID"""
        return Response({"http_method": "PATCH"})

    def destory(self, request, pk=None):
        """Handel getting data by its ID"""
        return Response({"http_method": "DELETE"})



class UsreProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profile"""
    serializer_class = serializers.UserProfileSeralizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)