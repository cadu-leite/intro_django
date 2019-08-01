from django.shortcuts import render


from django.views import View  # Class View
from django.views.generic.list import ListView  # generic Class Based List View
from django.http import HttpResponse  # para usar uma functon view simples

from django.utils import timezone  # usado no exemplo da GenClassBasedView

import datetime  # para mostrar a HORA como exemplo

from inscricao.models import Curso  # modelo de curso (listar cursos)


def agora_view(request):
    '''
    View para mostrar uma requisicao simples,
    e o que chega no HTTPResquest

    Toda requisição HTTP deve retornar um HttpResponse VÁLIDO!

    '''
    print(f"====>>>>> [ HTTP_USER_AGENT ] \n {request.META['HTTP_USER_AGENT']}")

    print(f"====>>>>> [ HTTP_USER_AGENT ] \n {request.headers['User-Agent']}")

    print(f"====>>>>> [ PATH ] \n {request.path}")
    print(f"====>>>>> [ COOKIES ] \n {request.COOKIES}")
    # outras variáveis disponiveis no request ... abaixo
    # https://docs.djangoproject.com/en/2.2/ref/request-response/

    now = datetime.datetime.now()
    html = "<html><body>Agora  = %s.</body></html>" % now
    return HttpResponse(html)

    # print request
    # print request.META


def cursos_list(request):
    '''
    Página SEM TEMPLATE para listar Cursos usando FUNCTION Views
    ----------------------------------------------
    LEMBRETE ... de padrão de nomenclatura de view
    <model>_list  <model>_form ou <model>_create
    <model_delete>  <model>_detail
    ----------------------------------------------
    '''

    # lista de cursos disponíveis.
    cursos = Curso.objects.all()

    # template par montar o html options
    option_template = "<li>{0}</li>"
    # str para montar a lista de  <option> curso </option>
    select_options = list(map(option_template.format, cursos))
    # tranforma list em string
    select_options = " ".join([item for item in select_options])

    # html final
    html = f"<html><body><ul>{select_options}</ul></body></html>"

    return HttpResponse(html)


# ============= Generic Class Based View
class AgoraView(View):
    '''
    Como a view "agora_view" só que uma classe
    '''
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        html = "<html><body>Agora  = %s.</body></html>" % now
        return HttpResponse(html)


class CursoListView(ListView):
    '''
    pagina de listagem de cusros (tosca)

    Uma ListView  ...
    https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-display/#listview

    Usa um template padrão

    '''
    model = Curso
    paginate_by = 3  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agora'] = timezone.now()
        return context


# User logado
# form enviado