from rest_framework.serializers import ModelSerializer
from .models import (
    LocationData,
    Region,
    State,
    City,
    Country
)

class RegionSerializer(ModelSerializer):
    class Meta:
        model=Region
        fields='__all__'
        
class CountrySerializer(ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'
        depth=1
        
        
class StateSerializer(ModelSerializer):
    class Meta:
        model=State
        fields ='__all__'
        depth=1
                
                
class CitySerializer(ModelSerializer):
    class Meta:
        model=City
        fields='__all__'
        depth=1
        
                     
class LocationSerializer(ModelSerializer):
    class Meta:
        model=LocationData
        fields ='__all__'
        depth=4
                               