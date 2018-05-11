from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
from django.shortcuts import render , get_object_or_404

# Create your views here.
#มีrequest ต้องมี response
from .models import Post


def go_to_home(request): 
    test ={
        "mi":"wew"
    }
    return render(request,"home.html",test)

def go_to_list(request): 
    data = Post.objects.all()
    connect = {
        "Post_data":data,
        "FIRST_NAME": "Miew",
        "LAST_NAME": "MOEW",
       } 
    return render(request, "index.html", connect)

def go_to_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instanse = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        print(form.cleaned_data.get("Comment"))
        instanse.save()
        messages.success(request,"Success Form was created ! ")
        return HttpResponseRedirect(instanse.get_absolute_url())
    else:
        messages.error(request,"Error : Failed to Create")
    #Check POST แบบ Hard Core
    # if request.method == "POST":
    #     print(request.POST) 

    Form = {
       "form" : form,
    } 
    return render(request, "form.html", Form)

def go_to_update(request,ids=None):
    inst = get_object_or_404(Post,id=ids)   
    form = PostForm(request.POST or None,instance=inst)
    if form.is_valid():
        inst = form.save(commit=False)
        inst.save()
        messages.success(request,"Success Edit !")
        return HttpResponseRedirect(inst.get_absolute_url())
    else:
        messages.error(request, "Error : Failed to Edit")

    Form = {
        "title":inst.title,
        "form": form,
        "instance":inst,
    }
    return render(request,"form.html",Form)

def go_to_detail(request,ids=None):
    static = get_object_or_404(Post, id=ids)
    connect = {
        "Topic": static.title,
        "static":static,
    }
    return render(request,"detail.html",connect)

def go_to_delete(request,ids=None):
    inst = get_object_or_404(Post,id=ids) 
    return render(request,"detail.html",connect)
