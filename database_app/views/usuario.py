# coding=utf-8

from django.http import HttpResponse
from django.template import RequestContext, loader
from database_app.models.usuario import Usuario


def inicio(request):
    if request.POST:
        login = request.POST['login']
        password = request.POST['password']
        user = Usuario.objects.filter(login=login, senha=password)
        if user:
            user = user[0]
            request.session['login'] = user.login
            request.session['nome'] = user.nome
            template = loader.get_template("welcome_page.html")
            context = RequestContext(request)
        else:
            template = loader.get_template("login_page.html")
            context = RequestContext(request, {
                'error_message': "Erro ao logar no sistema",
                'login': login,
                'password': password,
            })
        return HttpResponse(template.render(context))


def login(request):
    template = loader.get_template("login_page.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))