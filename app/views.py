from django.shortcuts import render
from django.conf import settings
import requests
from django.http import HttpResponse
import json


# Create your views here.

url=settings.URL

def create(request):
        if request.method=='POST':
                data=requests.get('{url}hotels'.format(url=url)).json()
                # print(data)
                return render(request,'create.html',{'data_list':data})
        else:
                data=requests.get('{url}hotels'.format(url=url)).json()
                # print(data)
                return render(request,'create.html',{'data_list':data})

