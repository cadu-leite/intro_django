from django.contrib import admin

from inscricao.models import Participante
from inscricao.models import Curso
from inscricao.models import Matricula


class ParticipanteAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'email')
    list_display = ('nome', 'email')
    list_display_links = ('nome', 'email')


# ... siga a PEP8
admin.site.register(Participante, ParticipanteAdmin)


admin.site.register(Curso)
# admin.site.register(Matricula)


class MatriculaAdmin(admin.ModelAdmin):
    fields = ('aluno', 'curso')
    list_display = ('aluno', 'curso')


# ... siga a PEP8
admin.site.register(Matricula, MatriculaAdmin)




# #Outra opção para registrar o Modelo no admin
# # ...
# from django.contrib import admin  # já presente no admin

# # import da sua Classe (model)
# from inscricao.models import Participante

# # atalho para registro
# admin.site.register(Participante)
