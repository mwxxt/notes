from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserViewSet, UserCustomUpdateDelete

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()), #получение токена
    path('', include(router.urls)), # все пользователи
    path('user/<int:id>/', UserCustomUpdateDelete.as_view()), # вывод одного пользователя
    
]