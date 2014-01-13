# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db.models import Q
from database_app.models.assunto import Assunto
from database_app.models.duvida import Duvida


@login_required
def index(request):
    subjects = Assunto.objects.all().order_by('nome')
    template = loader.get_template("forum_page.html")
    context = RequestContext(request, {
        'subjects': subjects,
    })
    return HttpResponse(template.render(context))


@login_required
def search(request):
    if request.POST:
        search = request.POST['search']
        # Obtendo todos os assuntos relacionados
        # as dúvidas existentes
        subjects = Assunto.objects.all().order_by('nome')
        # Obtendo as possíveis dúvidas relacionadas
        # com a busca realizada
        doubts = Duvida.objects.filter(Q(pergunta__icontains=search)).order_by('-dt_duvida')
        # Criando um dicionário com todos os
        # comentários das dúvidas relacionadas
        # key = duvida_id ; value = comentários
        dict_comments = {}
        for doubt in doubts:
            dict_comments[doubt.id] = doubt.comentario_set.all()
        if doubts:
            template = loader.get_template("forum_page.html")
            context = RequestContext(request, {
                'doubts': doubts,
                'subjects': subjects,
                'comments': dict_comments,
            })
        else:
            template = loader.get_template("forum_page.html")
            context = RequestContext(request, {
                'error_message': "Nenhum resultado encontrado! =(",
                'search': search,
                'subjects': subjects,
            })
        return HttpResponse(template.render(context))