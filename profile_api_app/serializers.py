from rest_framework import serializers
from . import models


class HelloSeralizer(serializers.Serializer):
    """Serialize name field for testing the APIVIEW"""
    name = serializers.CharField(max_length=20)


class UserProfileSeralizer(serializers.ModelSerializer):
    """Serializer for user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwarg = {"password":
                           {"write_only": True, "style":
                               {"input_type": "password"}
                            }
                       }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user