from django.db import models
from django.contrib.auth.models import User

class ForumCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="Category Title")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Forum Category"
        verbose_name_plural = "Forum Categories"

    def __str__(self):
        return self.title

class ForumThread(models.Model):
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE, related_name='threads', verbose_name="Category")
    title = models.CharField(max_length=255, verbose_name="Thread Title")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Thread Creator")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Forum Thread"
        verbose_name_plural = "Forum Threads"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE, related_name='posts', verbose_name="Thread")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Forum Post"
        verbose_name_plural = "Forum Posts"
        ordering = ['created_at']

    def __str__(self):
        return f"Post by {self.author.username} in thread '{self.thread.title}'"