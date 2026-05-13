from django.db import models
from django.contrib.auth.models import User

class GameServer(models.Model):
    name = models.CharField(max_length=50)
    rate = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    online_count = models.IntegerField(default=0)
    opening_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ВОТ ЭТОГО КЛАССА СЕЙЧАС НЕ ХВАТАЕТ:
class News(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Текст новости")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Это исправит заголовок в боковом меню и в списке объектов
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

class TopPlayer(models.Model):
    nickname = models.CharField(max_length=50)
    pvp = models.IntegerField(default=0)
    pk_count = models.IntegerField(default=0) # ИЗМЕНИ pk НА pk_count

    def __str__(self):
        return self.nickname

# Модель для персонажей в личном кабинете
class Character(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chars')
    name = models.CharField(max_length=16, unique=True)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    

class L2Server(models.Model):
    name = models.CharField(max_length=50)
    server_type = models.CharField(max_length=100)
    opening_date = models.CharField(max_length=100, blank=True)
    online_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='online') # 'online' или 'upcoming'

    def __str__(self):
        return self.name