from django.db import models

# Create your models here.

class Member(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,
    )
    member_name=models.CharField(max_length=1024)
    member_age=models.IntegerField()
    member_city=models.CharField(max_length=1024)
    member_image= models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return f"{self.member_name}, {self.member_age}"


class Specialist(models.Model):
    specialist_name=models.CharField(max_length=1024)
    specialist_Specialization=models.CharField(max_length=1024)
    specialist_city=models.CharField(max_length=512)
    specialist_phone=models.IntegerField()
    specialist_specialization_image=models.ImageField(upload_to="images/")
    specialist_image=models.ImageField(upload_to="images/")
    specialist_personal_page=models.URLField()
    specialist_rate=models.FloatField()
    specialist_confirmation=models.BooleanField()



    def __str__(self):
        return f"{self.specialist_name}, {self.specialist_Specialization}"


class Member_group(models.Model):
    group_name=models.CharField(max_length=1024)
    enter_counts=models.IntegerField()
    enter_total=models.IntegerField()
    missions_total=models.IntegerField()
    missions_counts=models.IntegerField()

class Group(models.Model):
    group_name=models.CharField(max_length=1024)
    member_number=models.IntegerField()
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    created_by=models.CharField(max_length=1024)
    missions_counts=models.IntegerField


class Mission(models.Model):
    mission_name=models.CharField(max_length=1024)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    mission_check=models.IntegerField()

class Post(models.Model):

    post_type_choices = models.TextChoices("Post Type", ["Article", "Story"])

    title = models.CharField(max_length=1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    is_published = models.BooleanField()
    post_type  = models.CharField(max_length=64, choices = post_type_choices.choices, default=post_type_choices.Article)

    def __str__(self) -> str:
        return f"{self.title}, {self.publish_date}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.name}, {self.content}"