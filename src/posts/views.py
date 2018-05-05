from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#มีrequest ต้องมี response



def go_to_home(request): 
    return HttpResponse("<h1>Home</h1>")

def go_to_list(request): 
      Name = {
        "FIRST_NAME": "Miew",
        "LAST_NAME": "MOEW",
    } 
    return render(request, "index.html", {Name})

def go_to_create(request): 
    return HttpResponse("<h1>Create</h1>")

def go_to_detail(request): 
    return HttpResponse("<h1>Detail</h1>")

def go_to_delete(request): 
    return HttpResponse("<h1>Delete</h1>")

def go_to_update(request): 
    return HttpResponse("<h1>update</h1>")