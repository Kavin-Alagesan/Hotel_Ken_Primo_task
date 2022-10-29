from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from .filters import *
from rest_framework import filters

class HotelsListCreateAPI(generics.ListCreateAPIView):
    queryset=HotelModel.objects.all()
    serializer_class=HotelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel_name','hotel_location']

