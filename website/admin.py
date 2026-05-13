from django.contrib import admin
from .models import GameServer, News, TopPlayer, Character

admin.site.register(GameServer)
admin.site.register(News)
admin.site.register(TopPlayer)
admin.site.register(Character)