
from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Participante(models.Model):
    '''
    1. Sempre Use CamelCase no nome do modelo
    2. Nunca use pluraiS no nome do modelo
    '''
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    # def __unicode__(self):
    def __str__(self):
        return "%s (%s)" % (self.nome, self.email)


class Curso(models.Model):
    '''
    Classe que define o Modelo CURSO
    Para que seja feita a matricula do participante.
    '''
    nome = models.CharField(max_length=150)

    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        '''
        '''
        return "%s (%s)" % (self.nome, self.data_inicio)


class Matricula(models.Model):
    '''
    Um aluno pode se matriular em 1 ou mais cursos.
    Essa tabela armazena as escolhas do aluno
    '''
    aluno = models.ForeignKey(
        'Participante', on_delete=models.SET_NULL, null=True
    )
    curso = models.ForeignKey(
        Curso, on_delete=models.SET_NULL, null=True
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s - %s)" % (self.aluno.nome, self.curso.nome, self.date)









