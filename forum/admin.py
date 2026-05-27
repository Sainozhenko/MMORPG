from django.contrib import admin
from .models import ForumCategory, ForumThread, ForumPost

@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(ForumThread)
class ForumThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creator', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title',)

@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'thread', 'created_at')
    search_fields = ('content',)