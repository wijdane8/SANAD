from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Specialist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    specialist_name=models.CharField(max_length=1024)
    specialist_specialization=models.CharField(max_length=1024,default="psycologist")
    specialist_city=models.CharField(max_length=512,default='')
    specialist_phone=models.IntegerField(default=0)
    specialist_specialization_image=models.ImageField(upload_to="pdfs/",default= '/media/images/OIP.jpeg')
    specialist_image=models.ImageField(upload_to="images/",default= '/media/images/OIP.jpeg')
    specialist_personal_page=models.URLField(default="")
    specialist_rate=models.FloatField(default=5)
    specialist_information=models.TextField()
    specialist_confirmation=models.BooleanField(default=False)
    type=models.CharField(max_length=512,default='specialist')


class Member(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    member_name=models.CharField(max_length=1024)
    member_age=models.IntegerField(default='')
    member_city=models.CharField(max_length=1024,default='')
    type=models.CharField(max_length=512)