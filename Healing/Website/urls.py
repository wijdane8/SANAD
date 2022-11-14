from django.urls import path
from . import views


app_name="Website"
urlpatterns=[
    path("home/",views.home,name="home"),
    #path("group_list/",views.list_view,name="list_view"),
    path("spiecilest_list/",views.spiecilest_list,name="spiecilest_list"),
    path("search/",views.search,name="search"),

    
]




