from django.contrib import admin
from app.models import Thread, Forum, UserProfile, Post

# Register your models here.
admin.site.register(Thread)
admin.site.register(Forum)
admin.site.register(UserProfile)
admin.site.register(Post)
