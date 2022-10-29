from django.urls import path
from .views import *

urlpatterns = [
    path('hotels/',HotelsListCreateAPI.as_view()),
]