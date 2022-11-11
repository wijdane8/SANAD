from django.urls import path
from . import views


app_name="Website"
urlpatterns=[
    path("home/",views.home,name="home"),
    
]




