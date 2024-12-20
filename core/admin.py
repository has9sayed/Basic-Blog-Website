from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'post', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username', 'post__title')
    ordering = ('-created_at',)