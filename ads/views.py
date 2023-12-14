from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .models import Location,Ad,VisitCount
from .serializers import AdSerializer, LocationSerializer, VisitCountSerializer
from datetime import date



class AdCreateView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
   
class AllAdView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        location = request.query_params.get('location')
        ads = Ad.objects.all()
        if location:
            ads = ads.filter(location__name__iexact=location)
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   
        
class AdDetailView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Ad.objects.filter(end_date__gte=date.today()).filter(start_date__lt=date.today()).get(pk=pk)
        except Ad.DoesNotExist:
            return None

    def get(self, request, pk):
        location = request.GET.get("location")
        if not location:
            return Response({'error': 'UnAuthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        ad = self.get_object(pk)
        if not ad:
            return Response({'error': 'Ad not found.'}, status=status.HTTP_404_NOT_FOUND)
        if ad.location.filter(name=location).count() == 0:
            return Response({'error': 'UnAuthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        today_date = date.today()
        visit_counter = VisitCount.objects.get_or_create(
            date=today_date,
            location=ad.location.get(name=location),
        )
        target_location = ad.location.get(name=location)
        if target_location.max_visitors > visit_counter.views_count:
            visit_counter.views_count += 1
            visit_counter.save()
            serializer = AdSerializer(ad)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'UnAuthorized'}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        ad = self.get_object(pk)
        if pk is not None:
            serializer = AdSerializer(ad, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, stauts=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Ad not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        ad = self.get_object(pk)
        if ad is not None:
            serializer = AdSerializer(ad, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Ad not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,  pk):
        ad = self.get_object(pk)
        if ad is not None:
            ad.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Ad not found.'}, status=status.HTTP_404_NOT_FOUND)     
    
    
    
       # Location Views
       
class LocationCreateView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LocationDetailView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return None

    def get(self, pk):
        location = self.get_object(pk)
        if location is not None:
            serializer = LocationSerializer(location)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'location not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        location = self.get_object(pk)
        if pk is not None:
            serializer = LocationSerializer(location, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, stauts=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'location not found.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        location = self.get_object(pk)
        if location is not None:
            serializer = AdSerializer(location, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Location not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,  pk):
        location = self.get_object(pk)
        if location is not None:
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Location not found.'}, status=status.HTTP_404_NOT_FOUND)