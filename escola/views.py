
from .models import Professor
from .serializers import ProfessorSerializer
from rest_framework import viewsets

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
