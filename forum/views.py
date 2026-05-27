from django.shortcuts import render, get_object_or_404
from .models import ForumCategory, ForumThread, ForumPost
from django.db.models import Count

def forum_home(request):
    categories = ForumCategory.objects.all()
    recent_threads = ForumThread.objects.all().order_by('-created_at')[:5]
    
    context = {
        'categories': categories,
        'recent_threads': recent_threads,
    }
    return render(request, 'forum/forum_home.html', context)

def thread_detail(request, thread_id):
    thread = get_object_or_404(ForumThread, id=thread_id)
    posts = thread.posts.all()
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})