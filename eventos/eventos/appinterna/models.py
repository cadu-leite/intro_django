from django.db import models

# Create your models here.
class Participante(models.Model):
    '''
    1. Sempre Use CamelCase no nome do modelo
    2. Nunca use pluraiS no nome do modelo
    '''
    HTML = "HTML"
    JS = "JS"
    PYTHON = "PYTHON"

    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)

    html = models.BooleanField(null=True, blank=True)
    js = models.BooleanField(null=True, blank=True)
    python = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.nome, self.email)


class Curso(models.Model):
    '''
    '''
    nome = models.CharField(max_length=150)

    data_inicio = models.DateField()
    data_fim = models.DateField()


class Matricula(models.Model):
    '''
    '''
    aluno = models.ForeignKey(
        'Participante', on_delete=models.SET_NULL, null=True
    )
    curso = models.ForeignKey(
        Curso, on_delete=models.SET_NULL, null=True
    )
    date = models.DateTimeField(auto_now_add=True)
