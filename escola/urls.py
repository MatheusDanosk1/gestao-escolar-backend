from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet, ProfessorViewSet, NotaViewSet, DisciplinaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'notas', NotaViewSet)
router.register(r'professores', ProfessorViewSet) 
router.register(r'disciplinas', DisciplinaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
