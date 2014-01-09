# coding=utf-8

from django.http import HttpResponse
from django.template import RequestContext, loader
from database_app.models.assunto import Assunto


def index(request):
    subjects = Assunto.objects.all()
    template = loader.get_template("forum_page.html")
    context = RequestContext(request, {
        'subjects': subjects,
    })
    return HttpResponse(template.render(context))