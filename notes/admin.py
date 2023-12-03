from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'formatted_datetime')  # Поля для отображения в списке
    list_filter = ('created_date',)  # Фильтры
    search_fields = ('title',)  # Поиск
    list_per_page = 20  # Количество записей на странице
    
    def formatted_datetime(self, obj):
        return obj.created_date.strftime('%d.%m.%Y %H:%M')

admin.site.register(Note, NoteAdmin)