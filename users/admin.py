from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')  # Поля для отображения в списке
    list_filter = ('username', 'first_name')  # Фильтры
    search_fields = ('username', 'first_name', 'last_name')  # Поиск
    list_per_page = 20  # Количество записей на странице

admin.site.register(CustomUser, UserAdmin)