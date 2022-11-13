from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from accounts.models import Specialist,Member
from django.contrib.auth.models import User

# Create your views here.
def home(request:HttpRequest):

    return render(request,"Website/index.html")
def spiecilest_list(request:HttpRequest):
    if "search" in request.GET:
        spiecilests= User.objects.all( Specialist.objects.filter(title__contains = "search"))
    else:
        spiecilests = Specialist.objects.all()

    
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request,"Website/list_view.html",{"spiecilests":spiecilests})