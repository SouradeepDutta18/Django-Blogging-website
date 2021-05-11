from django.contrib import admin
from .models import querypost
from .models import Blog
from .models import comment
from .models import UserProfile


# Register your models here.
admin.site.register(querypost)
admin.site.register(Blog)
admin.site.register(comment)
admin.site.register(UserProfile)