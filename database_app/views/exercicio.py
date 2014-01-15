# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from database_app.models.lista_exercicio import ListaExercicio


@login_required
def list_all(request):
    exercises = ListaExercicio.objects.all()
    dict_exercises = {}
    for ex in exercises:
        # Inserindo quebra de linha nas marcacoes de <br/>
        dict_exercises[ex.id] = ex.descricao.split('<br/>')
    template = loader.get_template("exercise_page.html")
    context = RequestContext(request, {
        'exercises': dict_exercises,
    })
    return HttpResponse(template.render(context))


@login_required
def show(request, exercicio_id, dict=None):
    # Obtendo a lista de exercício desejada
    if ListaExercicio.objects.filter(id=exercicio_id):
        exercise = ListaExercicio.objects.get(id=exercicio_id)
        # Inserindo quebra de linha nas marcacoes de <br/>
        desc = exercise.descricao.split('<br/>')
        # Obtendo todas as questões da lista de exercícios
        questions = exercise.questao_set.all()
        template = loader.get_template("question_page.html")
        dict_final = {
            'exercise_id': exercise.id,
            'description': desc,
            'questions': questions,
        }
        if dict:
            for i in dict:
                dict_final[i] = dict[i]
        context = RequestContext(request, dict_final)
    else:
        context = RequestContext(request)
    return HttpResponse(template.render(context))