from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("profile/", views.ProfileDashboardView.as_view(), name="profile"),
    path("create/", views.create_char, name="create_char"),
    path("rename/<int:char_id>/", views.rename_character, name="rename_char"),
    path("delete/<int:char_id>/", views.delete_char, name="delete_char"),
]
