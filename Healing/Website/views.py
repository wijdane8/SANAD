from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from accounts.models import Specialist,Member
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Website.models import Group,Post,Mission,Comment
# Create your views here.

def home(request:HttpRequest):
    if request.user.groups.filter(name='specialists').exists():
        return render(request,"Website/start_page.html")
    else:
        return render(request,"Website/base.html")

@login_required(login_url="/account/login/")
def my_group_list(request:HttpRequest):
    user=request.user.id
    groups=Group.objects.filter(member=Member.objects.get(user_id=user))
    
    return render(request,"Website/group_list.html",{"groups":groups})

def group_list(request:HttpRequest):
    groups=Group.objects.all()
    
    return render(request,"Website/group_list.html",{"groups":groups})




def new_group(request:HttpRequest):
    user=request.user.id
    if request.method == "POST":
        new_group = Group(specialist =Specialist.objects.get(user_id=user) , group_name= request.POST["group_name"], group_info=request.POST["group_info"], member_number=request.POST["member_number"], start_date=request.POST["start_date"],end_date=request.POST["end_date"],created_by=request.user.first_name+' '+request.user.last_name,missions_total='0',is_active=request.POST["is_active"])
        new_group.save()
        
        
    return render(request,"Website/new_group.html")

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




def new_mission(request:HttpRequest,group_id:int):
        try:
            group=Group.objects.get(id=group_id)
            
        except:
            msg="وصول غير مصرح به."
            return render(request,"Website/notfound.html",{"msg" : msg})
        return render(request,"Website/list_view.html",{"group":group})
        

def create_group(request:HttpRequest):
    user =request.user
    new_group=''
    
    if request.user.groups.filter(name='spiecialists').exists() and user.is_authenticated:
        if request.method == "POST":
            new_group= Group(group_name=request.POST["group_name"], group_info= request.POST["group_info"], member_number=request.POST["member_number"], start_date=request.POST["start_date"], end_date=request.POST["end_date"],created_by=user.first_name+' '+user.last_name)
            new_group.save()
            return redirect("Website:home")
    else:
        msg = "لا يمكن انشاء مجموعة جديدة الا بواسطة الأخصائي"
    return render(request,"Website/new_group.html",{"msg" : msg})
#post
def add_post(request : HttpRequest):
    user : User = request.user

    
    if user.is_authenticated:
        age = user.profile.age
        print(age)

    if not (user.is_authenticated and user.has_perm("Website.add_post")):
        return redirect("accounts:login_user")

    if request.method == "POST":
        new_post = Post(user = request.user, title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"], post_type=request.POST["post_type"] , image=request.FILES["image"])
        new_post.save()


    return render(request, "Website/add_post.html", {"Post" : Post})
    
def list_posts(request: HttpRequest):
    
    
    if "search" in request.GET:
        posts =post.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Post.objects.all()

    
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request, "Website/view_posts.html", {"posts" : posts})



def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post = post)
    except:
        return render(request , "Website/not_found.html")

    return render(request, "Website/post_detail.html", {"post" : post, "comments" : comments})


#update post
#if you want to use a decorator to check for login
@login_required(login_url="/account/login/")
def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Website/not_found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("Website:list_posts")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "Website/update_post.html", {"post" : post})


#delete post
def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "Website/not_found.html")

    post.delete()

    return redirect("Website:list_posts")




def add_comment(request: HttpRequest, post_id:int):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        new_comment = Comment(post=post, name = request.POST["name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("Website:post_detail", post.id)