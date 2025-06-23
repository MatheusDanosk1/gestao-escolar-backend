from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    formacao = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

