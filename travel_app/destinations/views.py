from django.shortcuts import render
from .serializers import DestinationSerializer, Destination
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class DestinationList(generics.ListAPIView):
    ''' This view retrive all the record from destination model '''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    

class DestinationCreate(generics.CreateAPIView):
    ''' This view create record in  destination model '''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationDetailView(generics.RetrieveAPIView):
    ''' This view retrive specific record in  destination model '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationUpdateView(generics.UpdateAPIView):
    ''' This view update record in  destination model '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationDeleteView(generics.DestroyAPIView):
    ''' This view delete record in  destination model '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer





