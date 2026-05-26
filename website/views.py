from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import L2Server, News, TopPlayer, Character
from . import services


def home(request):
    context = {
        "servers": L2Server.objects.all(),
        "news": News.objects.order_by("-created_at")[:5],
        "top_pvp": TopPlayer.objects.order_by("-pvp")[:5],
        "top_pk": TopPlayer.objects.order_by("-pk")[:5],
    }
    return render(request, "index.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


class ProfileDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        chars = services.get_player_characters(request.user.id)
        return render(request, "profile.html", {"chars": chars})


@login_required
def create_char(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Character.objects.create(owner=request.user, name=name)
        return redirect("profile")
    return render(request, "create_char.html")


@login_required
def rename_character(request, char_id):
    character = get_object_or_404(Character, id=char_id, owner=request.user)

    if request.method == "POST":
        new_name = request.POST.get("new_name")
        new_level = request.POST.get("new_level")
        if new_name:
            character.name = new_name
        if new_level:
            character.level = new_level

        character.save()

        return redirect("profile")

    return render(request, "rename_char.html", {"character": character})


@login_required
def delete_char(request, char_id):
    char = get_object_or_404(Character, id=char_id, owner=request.user)
    char.delete()
    return redirect("profile")