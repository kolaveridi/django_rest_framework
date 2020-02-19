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
    serializer_class=CountrySerializer
    
    def get_queryset(self):
        country_var=self.kwargs.get('country',None)
        queryset=self.queryset.filter(region__name=country_var) #look at region in country model and then name in Region model 
        return queryset
        
        