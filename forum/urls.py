from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum_home, name='home'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
]