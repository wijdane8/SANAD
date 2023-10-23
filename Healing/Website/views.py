from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from accounts.models import Specialist,Member
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from Website.models import Group,Post,Mission,Comment
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


def home(request:HttpRequest):
    names = Specialist.objects.all()
    return render(request,"Website/index.html",{'names':names})

@login_required(login_url="/account/login/")
def my_group_list(request:HttpRequest):
    is_specialist = Specialist.objects.filter(user_id=request.user.id).exists()
    user=request.user.id
    groups=Group.objects.filter(member=Member.objects.get(user_id=user))
    
    return render(request,"Website/group_list.html",{"groups":groups})

def group_list(request:HttpRequest):
    if "search" in request.GET:
        groups = Group.objects.filter(group_name__contains=request.GET["search"])
    else:
        groups=Group.objects.all()
    
    return render(request,"Website/group_list.html",{"groups":groups})

def join_group(request:HttpRequest,group_id:int):
    user=request.user
    group=Group.objects.get(id=group_id)
    group.member_number=group.member_number-1
    group.member.add(user.id)
    # permission = Permission.objects.create(name='can view '+group.group_name)
    # user.user_permissions.add(permission)
    
    return render(request, "Website/group_details.html", {"group" : group})




def new_group(request:HttpRequest):
    user=request.user.id
    if request.method == "POST":
        new_group = Group(specialist =Specialist.objects.get(user_id=user) , group_name= request.POST["group_name"], group_info=request.POST["group_info"], member_number=request.POST["member_number"], start_date=request.POST["start_date"],end_date=request.POST["end_date"],created_by=request.user.first_name+' '+request.user.last_name,missions_total='0',is_active=request.POST["is_active"])
        new_group.save()
        
        
    return render(request,"Website/new_group.html")

def search(request:HttpRequest):
    search=request.Post["search"]
    if Group.objects.filter(group_name__contains =search):
        names= Group.objects.filter(group_name__contains =search)
    else:
        names = Group.objects.all()
    return render(request,"Website/group_list.html",{"names":names})


def spiecilest_list(request:HttpRequest):
    try:
        names = Specialist.objects.all()
    except:
        msg="لاتوجد نتائج بحث"
        return render(request,"Website/notfound.html",{"msg" : msg})
    

    return render(request,"Website/list_view.html",{"names":names})

def members_list(request:HttpRequest):
    try:
        names = Member.objects.all()
    except:
        msg="لاتوجد نتائج بحث"
        return render(request,"Website/notfound.html",{"msg" : msg})
    

    return render(request,"Website/list_view.html",{"names":names})
    
def my_groups(request : HttpRequest , specialist_id : int):
    groups=Group.objects.filter(specialist_id=specialist_id)
    return render(request,"Website/group_list.html",{"groups":groups})

def contact_us(request:HttpRequest):
    msg=''
    if request.method=="POST":
         msg='تم الارسال'
    return render(request,"Website/contact_us.html",{'msg':msg})

def group_detail(request : HttpRequest, group_id : int):
    
    group = Group.objects.get(id=group_id)
    is_member = group.member.filter(user_id=request.user.id).exists()
 
    missions=Mission.objects.filter(group_id=group_id)
    try:
        if request.method == "POST":
            group.chat_url=request.POST["chat_url"]
            group.save()
            return redirect("Website:group_list")
    except:
        return render(request , "Website/notfound.html")

    return render(request, "Website/group_details.html", {"group" : group,"missions":missions, "is_member" : is_member})


def specialist_detail(request : HttpRequest, spcialist_id : int):

    try:
        specialist = Specialist.objects.get(pk=spcialist_id)
    except:
        return render(request , "Website/notfound.html")

    return render(request, "Website/specialist_detail.html", {"specialist" : specialist})


def my_missions(request:HttpRequest):
   # user=request.user
    #missions=mission.member.filter(member_id=user.id)
    #if request.method=='POST':
     #   new_mission=Mission(mission_check=["mission_check"])
      #  new_mission.save()
    pass
    return render(request,"Website/my_missions.html",{'missions':missions})
def new_mission(request:HttpRequest,group_id:int):
    group=Group.objects.get(id=group_id)
    missions=Mission.objects.filter(group_id=group_id)
    if request.method == "POST":
        try:
            new_mission=Mission(group=Group.objects.get(id=group_id),mission_name=request.POST["mission_name"],start_date=request.POST["start_date"],end_date=request.POST["end_date"])
            new_mission.save()
        except:
            msg="لايمكن انشاء المهمة."
            return render(request,"Website/notfound.html",{"msg" : msg})
    return render(request,"Website/new_mission.html",{"group":group,'missions':missions})




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
    is_specialist = Specialist.objects.filter(user_id=request.user.id).exists()
    if user.is_authenticated:
        if request.method == "POST":
            new_post = Post(user = request.user, title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = True, post_type=request.POST["post_type"] , image=request.FILES["image"])
            new_post.save()
    else:
        return redirect("accounts:login_user")

    return render(request, "Website/add_post.html", {"Post" : Post,'is_specialist':is_specialist})
    
def list_posts(request: HttpRequest):
        error_msg=''
        if "search" in request.GET:
            posts =Post.objects.filter(title__contains=request.GET["search"])
        else:
            try:
                if Post.objects.filter(post_type="Story ").exists():
                    posts =Post.objects.filter(post_type="Story ")
                else:
                    error_msg='لاتوجد مواضيع لعرضها'
            except:
                error_msg="نأسف هناك خطأ"

        return render(request, "Website/view_posts.html", {"posts" : posts,'error_msg':error_msg})

def list_posts_artical(request: HttpRequest):
    error_msg=''
    if Post.objects.filter(post_type="Article").exists():
       posts=Post.objects.filter(post_type="Article")
    else:
        error_msg='لاتوجد مواضيع لعرضها'
    

    return render(request, "Website/view_posts.html",{"posts" : posts,'error_msg':error_msg})



def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post = post)
    except:
        return render(request , "Website/notfound.html")

    return render(request, "Website/post_detail.html", {"post" : post, "comments" : comments})



def add_comment(request: HttpRequest, post_id:int):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        new_comment = Comment(post=post, name = request.POST["name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("Website:post_detail", post.id)