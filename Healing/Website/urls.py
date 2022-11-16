from django.urls import path
from . import views


app_name="Website"
urlpatterns=[
    path("home/",views.home,name="home"),
    path("create_group/",views.create_group,name="create_group"),
    path("spiecilest_list/",views.spiecilest_list,name="spiecilest_list"),
    path("search/",views.search,name="search"),
    path("create_group/",views.create_group,name="create_group"),
    #path("profile/",views.profile,name="profile"),
    path("group_list/",views.group_list,name="group_list"),
    path("my_group_list/",views.my_group_list,name="my_group_list"),
    path("new_group/",views.new_group,name="new_group"),
    path("new_mission/<group_id>",views.new_mission,name="new_mission"),
    path("post/add/", views.add_post, name="add_post"),
    path("post/list/", views.list_posts, name="list_posts"),
    path("post/detail/<post_id>/", views.post_detail, name="post_detail"),
    path("post/update/<post_id>/", views.update_post, name="update_post"),
    path("post/delete/<post_id>/", views.delete_post, name="delete_post"),

    path("post/<post_id>/comment/new/", views.add_comment, name="add_comment")
    
    
]




