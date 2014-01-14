# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from database_app.models.lista_exercicio import ListaExercicio


@login_required
def list_all(request):
    exercises = ListaExercicio.objects.all()
    template = loader.get_template("exercise_page.html")
    context = RequestContext(request, {
        'exercises': exercises,
    })
    return HttpResponse(template.render(context))


@login_required
def show(request, exercicio_id):
    # Obtendo a lista de exercício desejada
    exercise = ListaExercicio.objects.get(id=exercicio_id)
    # Obtendo todas as questões da lista de exercícios
    questions = exercise.questao_set.all()
    template = loader.get_template("question_page.html")
    context = RequestContext(request, {
        'exercise': exercise,
        'questions': questions
    })
    return HttpResponse(template.render(context))