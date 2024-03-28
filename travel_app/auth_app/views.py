from django.shortcuts import render
from .serializers import UserSerializer, User
from rest_framework import generics
# Create your views here.

class UserCreate(generics.CreateAPIView):
    ''' This view add user in User model '''
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
