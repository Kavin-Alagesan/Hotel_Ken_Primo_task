from django.urls import path
from .views import *

urlpatterns = [
    path('',create,name="create"),
]
