# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from database_app.models.duvida import Duvida
from database_app.models.usuario import Usuario
from datetime import datetime


@login_required
def add(request):
    if request.POST:
        doubt = request.POST['doubt']
        login = request.user
        u = Usuario.objects.get(login=login)
        d = Duvida()
        d.login_usuario = u
        d.dt_duvida = datetime.now()
        d.pergunta = doubt
        d.save()
        template = loader.get_template("forum_page.html")
        context = RequestContext(request)
        return HttpResponse(template.render(context))