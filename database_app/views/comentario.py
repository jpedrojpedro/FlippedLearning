# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from database_app.models.comentario import Comentario
from database_app.models.duvida import Duvida
from database_app.models.usuario import Usuario
from datetime import datetime


@login_required
def add(request):
    if request.POST:
        comment = request.POST['comment']
        doubt = request.POST['doubt']
        login = request.user
        d = Duvida.objects.get(id=int(doubt))
        u = Usuario.objects.get(login=login)
        c = Comentario()
        c.id_duvida = d
        c.login_usuario = u
        c.texto_comentario = comment
        c.dt_comentario = datetime.now()
        c.save()
        template = loader.get_template("forum_page.html")
        context = RequestContext(request)
        return HttpResponse(template.render(context))