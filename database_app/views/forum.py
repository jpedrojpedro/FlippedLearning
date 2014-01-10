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
        results = Duvida.objects.filter(Q(pergunta__icontains=search)).order_by('-dt_duvida')
        subjects = Assunto.objects.all().order_by('nome')
        if results:
            template = loader.get_template("forum_page.html")
            context = RequestContext(request, {
                'results': results,
                'subjects': subjects,
            })
        else:
            template = loader.get_template("forum_page.html")
            context = RequestContext(request, {
                'error_message': "Nenhum resultado encontrado! =(",
                'search': search,
                'subjects': subjects,
            })
        return HttpResponse(template.render(context))