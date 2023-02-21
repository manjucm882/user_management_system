from django.shortcuts import render
from rest_framework import generics
from myapp.models import User
from myapp.serializers import UserSerializer


# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

