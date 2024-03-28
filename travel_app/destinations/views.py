from django.shortcuts import render
from .serializers import DestinationSerializer, Destination
from rest_framework import generics
# Create your views here.

class DestinationList(generics.ListAPIView):
    ''' This view retrive all the record from destination model '''
    
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationCreate(generics.CreateAPIView):
    ''' This view create record in  destination model '''
    
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer





