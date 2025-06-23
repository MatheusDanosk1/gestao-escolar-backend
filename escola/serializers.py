from rest_framework import serializers
from .models import Aluno

from .models import Professor
from rest_framework import serializers

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

from .models import Disciplina
from rest_framework import serializers

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


