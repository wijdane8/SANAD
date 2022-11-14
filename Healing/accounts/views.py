from django.shortcuts import render, redirect
from django.http import HttpRequest
from Website.models import Specialist,Member
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_specialist(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
        
        name=new_user.first_name+''+new_user.last_name

        new_specialist=Specialist(user=new_user,specialist_name=name,specialist_specialization=request.POST["specialist_specialization"],specialist_image=request.FILES["specialist_image"],specialist_specialization_image=request.FILES["specialist_specialization_image"],specialist_city=request.POST["specialist_city"],specialist_phone=request.POST["specialist_phone"],specialist_personal_page=request.POST["specialist_personal_page"])
        new_specialist.save()
    return render(request, "accounts/login.html")



def register_member(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
        name=new_user.username
        new_member= Member(user=new_user,member_name=name,member_age=request.POST["member_age"],member_image=request.FILES["member_image"],member_city=request.POST["member_city"])
        new_member.save()
    return render(request, "accounts/member_register.html")

def register_type(request : HttpRequest):

    if request.method == "POST":
        if request.POST["register_type"]=="specialist":
            return render(request, "accounts/specialist_register.html")
        else:
             request.POST["register_type"]=="member"
        return render(request, "accounts/member_register.html")
       
    return render(request, "accounts/register_type.html")

def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("Website:home")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "accounts/login.html", {"msg" : msg})


def logout_user(request: HttpRequest):

    logout(request)

    return redirect("Website:home")

    