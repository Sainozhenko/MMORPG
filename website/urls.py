from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('character/new/', views.create_char, name='create_char'),
    path('character/<int:char_id>/rename/', views.rename_char, name='rename_char'),
    path('character/<int:char_id>/delete/', views.delete_char, name='delete_char'),
]