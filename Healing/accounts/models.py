from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Specialist(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,)
    specialist_specialization=models.CharField(max_length=1024)
    specialist_city=models.CharField(max_length=512)
    specialist_phone=models.IntegerField()
    specialist_specialization_image=models.ImageField(upload_to="images/")
    specialist_image=models.ImageField(upload_to="images/")
    specialist_personal_page=models.URLField()
    specialist_rate=models.FloatField()
    specialist_confirmation=models.BooleanField()

class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,
    )
    member_age=models.IntegerField()
    member_city=models.CharField(max_length=1024)
    member_image= models.ImageField(upload_to="images/")