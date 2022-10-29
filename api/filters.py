import django_filters
from .models import *

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model=HotelModel
        fields=['hotel_name','hotel_location']

