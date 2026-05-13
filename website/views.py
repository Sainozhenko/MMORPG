from django.shortcuts import render, redirect, get_object_or_404
from .models import L2Server, News, TopPlayer, Character
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'servers': L2Server.objects.all(), 
        'news': News.objects.order_by('-created_at')[:5],
        'top_pvp': TopPlayer.objects.order_by('-pvp')[:5],
        'top_pk': TopPlayer.objects.order_by('-pk')[:5],
    }
    return render(request, 'index.html', context)

# Регистрация (чтобы работало по ссылке в urls.py)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Личный кабинет
@login_required
def profile(request):
    chars = Character.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'chars': chars})

# Функции CRUD для персонажей (create, rename, delete)
@login_required
def create_char(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Character.objects.create(owner=request.user, name=name)
        return redirect('profile')
    return render(request, 'create_char.html')

@login_required
def rename_char(request, char_id):
    char = get_object_or_404(Character, id=char_id, owner=request.user)
    if request.method == "POST":
        char.name = request.POST.get('new_name')
        char.save()
        return redirect('profile')
    return render(request, 'rename_char.html', {'char': char})

@login_required
def delete_char(request, char_id):
    char = get_object_or_404(Character, id=char_id, owner=request.user)
    char.delete()
    return redirect('profile')