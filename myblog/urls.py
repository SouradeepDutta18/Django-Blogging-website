from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
   path("",views.home,name="bloghome"),
    path("posts/<int:post_id>/",views.blogpost,name="BlogPost"),
    path("posts/postComment/",views.postComment,name="BlogComment"),
     path("upload/",views.upload,name="BlogUpload"),
     path("profile/",views.profile,name="profile")
]