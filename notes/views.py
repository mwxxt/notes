from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()