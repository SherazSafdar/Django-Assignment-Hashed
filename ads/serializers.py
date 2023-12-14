from rest_framework import serializers
from .models import Location,Ad,VisitCount

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
        
class VisitCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitCount
        fields = '__all__'