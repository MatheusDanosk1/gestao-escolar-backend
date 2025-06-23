from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    formacao = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome

class Nota(models.Model):
    valor = models.FloatField()
    data_lancamento = models.DateField()
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='notas')

    def __str__(self):
        return f"{self.aluno.nome} - {self.valor}" 
