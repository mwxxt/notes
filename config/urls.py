
from django.contrib import admin
from django.urls import path, include
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls), #админ панель
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path("api/", include('users.urls')), #Отображение всех пользователей
]
