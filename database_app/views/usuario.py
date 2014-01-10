# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader


@login_required
def inicio(request):
    template = loader.get_template("welcome_page.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))