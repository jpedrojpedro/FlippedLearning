# coding=utf-8

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template("welcome_page.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def login(request):
    template = loader.get_template("login_page.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))