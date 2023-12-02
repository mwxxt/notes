from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UserCustomUpdateDelete

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)), # все пользователи
    path('user/<int:id>/', UserCustomUpdateDelete.as_view()), # вывод одного пользователя
]