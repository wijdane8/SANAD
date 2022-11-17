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
    path("my_missions/",views.my_missions,name="my_missions"),
    path("my_group_list/",views.my_group_list,name="my_group_list"),
    path("my_groups/<specialist_id>",views.my_groups,name="my_groups"),
    path("new_group/",views.new_group,name="new_group"),
    path("new_mission/<group_id>",views.new_mission,name="new_mission"),
    path("join_group/<group_id>",views.join_group,name="join_group"),
    #path("my_mission/",views.my_mission,name="my_mission"),
    path("post/add/", views.add_post, name="add_post"),
    path("post/list/", views.list_posts, name="list_posts"),
    path("post/articals/", views.list_posts_artical, name="list_posts_artical"),
    path("post/detail/<post_id>/", views.post_detail, name="post_detail"),
    path("specialist_detail/<spcialist_id>/", views.specialist_detail, name="specialist_detail"),
    path("post/<post_id>/comment/new/", views.add_comment, name="add_comment"),
    path("group_detail/<group_id>/", views.group_detail, name="group_detail"),
    path("contact_us/", views.contact_us, name="contact_us"),
    
    
]




