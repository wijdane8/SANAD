from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from accounts.models import Specialist,Member
from django.contrib.auth.models import User

# Create your views here.
def home(request:HttpRequest):

    return render(request,"Website/index.html")
def search(request:HttpRequest):
    if "search" in request.GET:
        try:
            names= Specialist.objects.filter(specialist_name__contains ='search')
        except:
            msg="لاتوجد نتائج بحث"
            return render(request,"Website/notfound.html",{"msg" : msg})
    else:
        names = Specialist.objects.all()

    return render(request,"Website/search.html",{"names":names})


def spiecilest_list(request:HttpRequest):
    try:
        names = Specialist.objects.all()
    except:
        msg="لاتوجد نتائج بحث"
        return render(request,"Website/notfound.html",{"msg" : msg})
    

    return render(request,"Website/list_view.html",{"names":names})
def spiecialist_check(request:HttpRequest):
    user : User = request.user
    if user.is_authenticated:
        try:
            name = user.Specialist.specialist_name
        except:
            msg="وصول غير مصرح به."
        return render(request,"Website/notfound.html",{"msg" : msg})

        
@spiecialist_check(login_url="/Website/home")
def create_group(request:HttpRequest):
    pass
