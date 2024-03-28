from rest_framework import serializers
from .models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    ''' Deserialize incoming deta with request and serialize outgoing 
        data with response '''
    
    class Meta:
        model = Destination
        fields = "__all__"
    
    
    def validate_city(self, value):
        """ Validate the city field."""
        if not value.isalpha():
            raise serializers.ValidationError("City must contain only alphabetical characters.")
        return value
    