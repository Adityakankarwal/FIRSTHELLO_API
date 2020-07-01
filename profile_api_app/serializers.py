from rest_framework import serializers

class HelloSeralizer(serializers.Serializer):
    "Seralize name field for testing the APIVIEW"
    name = serializers.CharField(max_length=20)