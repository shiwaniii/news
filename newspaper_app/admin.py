from django.contrib import admin

from newspaper_app.models import Category, Comment, Post, Tag, UserProfile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Comment)