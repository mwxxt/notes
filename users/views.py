from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import CustomUser
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def perform_create(self, serializer):
        password = make_password(self.request.data.get('password'))
        serializer.save(password=password)
    
class UserCustomUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'id'