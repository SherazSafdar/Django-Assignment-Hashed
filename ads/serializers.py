from rest_framework import serializers
from .models import Location,Ad

class LocationSerializer(serializers.ModelSerializer):
    class Mete:
        model = Location
        fields = ['name', 'max_visitors', 'current_visitor']
        
class AdSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ad
        fields = ['name', 'start_date', 'end_date', 'locations']