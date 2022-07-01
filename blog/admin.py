from django.contrib import admin
from .models import Post # берем модель (объект) из того модуля

admin.site.register(Post) #регистрируем модель
