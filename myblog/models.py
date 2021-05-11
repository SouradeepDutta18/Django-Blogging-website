from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django import forms

# Create your models here.
class querypost(models.Model):
    query_id=models.AutoField
    email=models.CharField(max_length=25,default="")
    name=models.CharField(max_length=35,default="")
    contact_no=models.CharField(max_length=11,default="")
    query=models.TextField(default="")

    def __str__(self):
        return self.query
class Blog(models.Model):
      post_id=models.AutoField(primary_key=True)
      post_title=models.CharField(max_length=70,default="")
      pub_date=models.DateField(auto_now_add=True)
      author_name=models.CharField(max_length=30,default="")
      content=models.CharField(max_length=5000,default="")
      thumbnail=models.ImageField(upload_to="blog/images",default="")
      video_id=models.CharField(max_length=50,default="",blank=True)
      viewer_count=models.IntegerField(default=0)
      
      def __str__(self):
          return self.post_title
class UserProfile(models.Model):
    user   = models.ForeignKey(User,default="",on_delete=models.CASCADE,primary_key=True)
    dp = models.ImageField(upload_to="blog/profile",default="",blank=True)
    def __str__(self):
        return self.user.first_name
class comment(models.Model):
      sno=models.AutoField(primary_key=True)
      post=models.ForeignKey(Blog,on_delete=models.CASCADE)
      timestamp=models.DateTimeField(default=now)
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      content=models.TextField()
      parent=models.ForeignKey('self',null=True,on_delete=models.CASCADE)
      def __str__(self):
          return self.content[0:25]+"..."
class form(forms.ModelForm):
    model=Blog


