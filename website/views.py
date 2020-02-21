from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from . serializer import *
from .models import *

# Create your views here.
class RegionListApiView(ListAPIView):
    queryset=Region.objects.all()
    serializer_class=RegionSerializer
    
class CountryListApiView(ListAPIView):
    queryset=Country.objects.all()
    print("top",queryset)
    serializer_class=CountrySerializer
    
    def get_queryset(self):
        region_var=self.kwargs.get('region',None)
        queryset=self.queryset.filter(region__name=region_var) #look at region in country model and then name in Region model 
        print("queryset is ",list(queryset))
        print("len",len(queryset))
        for x in range(len(queryset)):
           print(queryset[x])

        return queryset
        
 
class StateListApiView(ListAPIView):
    queryset=State.objects.all()
    serializer_class=StateSerializer
   
    def get_queryset(self):
        region_var=self.kwargs.get('region',None)
        country_var=self.kwargs.get('country',None)
        queryset=self.queryset.filter(country__name=country_var,country__region__name=region_var)
        return queryset
        
    
  
class CityListApiView(ListAPIView):
     queryset=City.objects.all()
     serializer_class=CitySerializer
     def get_queryset(self):
        region_var=self.kwargs.get('region',None)
        country_var=self.kwargs.get('country',None)
        state_var=self.kwargs.get('state',None)
        queryset=self.queryset.filter(state__name=state_var,state__country__name=country_var,state__country__region__name=region_var)
        return queryset
         
               
       
class LocationDataListApiView(ListAPIView):
    queryset=LocationData.objects.all()
    serializer_class=LocationSerializer
    def get_queryset(self):
        region_var=self.kwargs.get('region',None)
        country_var=self.kwargs.get('country',None)
        state_var=self.kwargs.get('state',None)
        city_var=self.kwargs.get('city',None)
        queryset=self.queryset.filter(
            city__name=city_var,
            city__state__country__name=country_var,
            city__state__country__region__name=region_var,
            city__state__name=state_var
            )
        return queryset
               
           
           
           
           