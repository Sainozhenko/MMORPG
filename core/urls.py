# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # ИМПОРТ НАСТРОЕК
from django.conf.urls.static import static # ИМПОРТ ФУНКЦИИ СТАТИКИ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), # Подключаем файл, который мы написали выше
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Вот здесь это должно жить:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)