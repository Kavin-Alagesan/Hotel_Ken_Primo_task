
from django.db import models

# Create your models here.
class HotelModel(models.Model):
    CHOICE_TYPE=[
        ("APPARTMENT","APPARTMENT"),
        ("RESORT","RESORT"),
        ]
    CHOICE_RATINGS=[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ]
    CHOICE_LOCATION=[
        ("TN","TN"),
        ("KERALA","KERALA"),
        ("KA","KA"),
        ]
    hotel_id=models.AutoField(primary_key=True)
    hotel_name=models.CharField(max_length=100)
    hotel_location=models.CharField(max_length=30,choices=CHOICE_LOCATION)
    hotel_description=models.CharField(max_length=50)
    hotel_type=models.CharField(max_length=50,choices=CHOICE_TYPE)
    hotel_image=models.ImageField(upload_to='hotel_image',null=True,blank=True)
    hotel_rating=models.PositiveIntegerField(choices=CHOICE_RATINGS)

    def __str__(self):
        return f"{self.hotel_name} : {self.hotel_location}"