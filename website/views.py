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