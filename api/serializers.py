from rest_framework import serializers
from .models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelModel
        fields=['hotel_name','hotel_location','hotel_description','hotel_type','hotel_image','hotel_rating']

    