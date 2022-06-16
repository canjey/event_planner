from multiprocessing import Event
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Events
from .serializers import UserSerializer, NewUserSerializer, NewEventSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = NewUserSerializer

class NewEventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = NewEventSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
 