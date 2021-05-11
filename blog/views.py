from django.http import HttpResponse
from django.shortcuts import render,redirect
from myblog.models import querypost
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.core.files.storage import FileSystemStorage
from myblog.models import UserProfile
from myblog.models import Blog
import os
def home(request):
    blogs = Blog.objects.all().order_by("-viewer_count")
    len=blogs.count()
    blogs=blogs[:len//2]
    print("blogs:",blogs)
    return render(request,"abc.html",{"blogs":blogs})
def search(request):
    
    if(request.method=="POST"):
        query=request.POST.get("query")    
        blogs = Blog.objects.filter(post_title__contains=query)
        print("blogs:",blogs)
        xyz=Blog.objects.filter(content__contains=query)
        print("xyz:",xyz)
        blogs=blogs.union(xyz)
        
        abc=Blog.objects.filter(author_name__contains=query)
        print("abc:",abc)
        blogs=blogs.union(abc)
        print("blogs:",blogs)

        return render(request,"blog/home.html",{"blogs":blogs})
    else:    
     return redirect("/")

    
def contact(request):
    if(request.method=="POST"):
          Name=request.POST.get("Name")
          email=request.POST.get("email")
          phone=request.POST.get("phone")
          query=request.POST.get("cause")
          new_query=querypost(email=email,contact_no=phone,name=Name,query=query)
          new_query.save()
          messages.success(request,"Your response have been saved")
          return redirect("/")


    return render(request,"contact.html")
def signup(request):
    if(request.method=="POST"):
         username=request.POST.get("username")
         email=request.POST.get("email")
         fName=request.POST.get("fName")
         lName=request.POST.get("lName")
         password1=request.POST.get("password1")
         password2=request.POST.get("password2")
         print(username,email,fName,lName,password1,password2)
         if(password1 != password2):
             print("true")
             messages.success(request,"your two passwords don't match. Please type again.")
             return redirect("/")
         elif(fName=="" or lName==""):
             print("true")
             messages.success(request,"First name or last Name can not be blank.")
             return redirect("/")
         else:
            user = User.objects.create_user(username, email, password1)
            user.last_name = lName
            user.first_name=fName
            user.save()
            print(user)
            messages.success(request,"you are signed up")
            return redirect("/")

    else:
      return render(request,"signup.html")
def loginUser(request):
     if(request.method=="POST"):
         username=request.POST.get("username")
         password=request.POST.get("password")
         print(username,password)
         from django.contrib.auth import authenticate
         user = authenticate(username=username, password=password)
         if user is not None:
             login(request,user)
             messages.success(request,"You are logged in")
             return redirect("/")
         else:
             messages.error(request,"you are not a registered user. sign up to continue")
             return redirect("/signup")
             
     return render(request,"login.html")
def logoutUser(request):
    logout(request)
    messages.success(request,"You are logged out")
    return redirect("/")


