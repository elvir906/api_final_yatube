from django.contrib import admin
from .models import Comment, Post, Group, Follow

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
