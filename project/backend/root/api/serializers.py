from django.shortcuts import render

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Events


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

# Used to hash users password

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class NewEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__' 