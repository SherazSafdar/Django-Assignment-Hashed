from rest_framework import viewsets
from rest_framework import generics
from .models import Location,Ad,VisitCount
from .serializers import AdSerializer, LocationSerializer, VisitCountSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AdListView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class LocationListView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class VisitCountListView(generics.ListCreateAPIView):
    queryset = VisitCount.objects.all()
    serializer_class = VisitCountSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class VisitCountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisitCount.objects.all()
    serializer_class = VisitCountSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]