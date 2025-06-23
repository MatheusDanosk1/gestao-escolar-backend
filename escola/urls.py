from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, ProfessorViewSet, DisciplinaViewSet, NotaViewSet, TurmaViewSet

router = DefaultRouter()
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet) 
router.register(r'notas', NotaViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
