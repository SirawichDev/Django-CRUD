from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#มีrequest ต้องมี response



def go_to_home(request): 
    return HttpResponse("<h1>Home</h1>")