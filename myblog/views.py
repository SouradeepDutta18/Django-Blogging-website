from django.shortcuts import render
from .models import Blog
from .models import UserProfile
from .models import comment
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.timezone import now
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os


from django.contrib.auth.models import User

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by("-viewer_count")
    return render(request,"blog/home.html",{"blogs":blogs})
def blogpost(req,post_id):
    blog = Blog.objects.filter(post_id=post_id)[0]
    print(blog)

    comments=comment.objects.filter(post=blog,parent=None).order_by(("-timestamp"))
    replies = comment.objects.filter(post=blog).exclude(parent=None).order_by(("-timestamp"))
    print("replies:",replies)
    replydict={}
    for reply in replies:
        if(reply.parent.sno not in replydict.keys()):
            replydict[reply.parent.sno]=[reply]
        else:
            replydict[reply.parent.sno].append(reply)
    print("replydict:",replydict)
    
    print(comments)
    blog.viewer_count+=1
    blog.save()
    return render(req,"blog/blogpost.html",{"blog":blog,"comments":comments,"replydict":replydict})
def postComment(request):
    if(request.method=="POST"):
        content = request.POST.get("comment")
        user=request.user
        print(user)
        post_id=request.POST.get("post_id")
        print(post_id)
        post=Blog.objects.get(post_id=post_id)
        parent=request.POST.get("parent_comment_sno")
        if(parent!=None):
            timestamp=timezone.now()
            parent=comment.objects.get(sno=parent)
            print(parent)
            new_comment=comment(post=post,user=user,content=content,parent=parent,timestamp=timestamp)
            new_comment.save()
            #messages.success(request,"Your Reply has been posted")
        else:
            new_comment=comment(post=post,user=user,content=content)
            new_comment.save()
            #messages.success(request,"Your comment has been posted")
        print(new_comment)
        return redirect(f"/blog/posts/{post_id}")
def upload(request):
    BASE_DIR=os.getcwd()
    print("BASE_DIR:",BASE_DIR)
    location=os.path.join(BASE_DIR, 'media/blog/images')
    if(request.method=="POST"):
        myfile = request.FILES['image']
        post_title=request.POST.get("post_title")
        author_name=request.user.username
        content=request.POST.get("content")
        video_id=request.POST.get("video_id")
        fs = FileSystemStorage(location=location)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = f"/media/blog/images/{filename}"
        print(uploaded_file_url,post_title,author_name,content,video_id)
        if(video_id!=""):
            new_post=Blog(post_title=post_title,author_name=author_name,content=content,video_id=video_id)
            new_post.thumbnail = f"blog/images/{filename}"
            new_post.save()
        else:
            new_post=Blog(post_title=post_title,author_name=author_name,content=content)
            new_post.thumbnail = f"blog/images/{filename}"
            new_post.save()
        messages.success(request,"Your post has been published.")
        return redirect("/")
    return render(request,"blog/create.html")
def profile(request):
    BASE_DIR=os.getcwd()
    print("BASE_DIR:",BASE_DIR)
    location=os.path.join(BASE_DIR, 'media/blog/profile')
    try:
            user = UserProfile.objects.get(user=request.user)
    except Exception as e:
            user = None
    
    if(request.method=="POST"):
        
        
        print(f"BASE_DIR:{BASE_DIR},location:{location}")
       
        myfile=request.FILES["image"]
        fs=FileSystemStorage(location=location)
        filename = fs.save(myfile.name, myfile)
        
        
        if(user==None):
            new_profile=UserProfile(user=request.user)
            new_profile.dp = f"blog/profile/{filename}"
            new_profile.save()
            image=UserProfile.objects.filter(user=request.user)[0].dp
            user=True
        else:
            obj=UserProfile.objects.filter(user=request.user)[0]
            
            obj.dp=f"blog/profile/{filename}"
            obj.save()
            image=UserProfile.objects.filter(user=request.user)[0].dp
            print("image:",image)


        
    blogs = Blog.objects.filter(author_name=request.user.username)
    print("blogs:",blogs)
    if(user == None):
        return render(request,"profile.html",{"image":False,"blogs":blogs})
    else:
        return render(request,"profile.html",{"image":UserProfile.objects.filter(user=request.user)[0].dp,"blogs":blogs})
        
