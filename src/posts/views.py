from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def direct_home(request): #มีrequest ต้องมี response
    return HttpRequest("<h1>Home</h1>")