from django.http import HttpResponse

from django.shortcuts import render , get_object_or_404

# Create your views here.
#มีrequest ต้องมี response
from .models import Post


def go_to_home(request): 
    return HttpResponse("<h1>Home</h1>")

def go_to_list(request): 
    data = Post.objects.all()
    connect = {
        "Post_data":data,
        "FIRST_NAME": "Miew",
        "LAST_NAME": "MOEW"
       } 
    return render(request, "index.html", connect)

def go_to_create(request): 
    Name = {
        "FIRST_NAME": "Miewss",
        "LAST_NAME": "MOEW"
    } 
    return render(request, "index.html", Name)

def go_to_detail(request): 
    static = get_object_or_404(Post, id=2)
    connect = {
        "static":static,
    }
    return render(request,"detail.html",connect)

def go_to_delete(request): 
    return HttpResponse("<h1>Delete</h1>")

def go_to_update(request): 
    return HttpResponse("<h1>update</h1>")