# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from django.db.models import Max
from django.db.utils import DatabaseError
from database_app.models.questao import Questao
from database_app.models.instancia import Instancia
from database_app.models.esquema import Esquema
from database_app.models.usuario import Usuario
from database_app.models.resposta import Resposta
from database_app.models.lista_exercicio import ListaExercicio
from database_app.views.exercicio import show
from datetime import datetime

@login_required
def verificar(request, exercicio_id, questao_id):
    if request.POST:
        answer = request.POST['resposta']
        # Obtendo a questão respondida
        q = Questao.objects.get(id=questao_id)
        schema_name = "%s_%s" % (q.nome_esquema, request.user)
        login = "%s" % request.user
        # Verificando se a instancia existe
        i = Instancia.objects.filter(nome_esquema=q.nome_esquema, login_usuario=login)
        # Caso em que a instancia existe
        if i:
            trocar_esquema(schema_name)
            result = comparar_respostas(answer, q.resposta_gabarito)
        # Caso em que a instancia não existe
        else:
            e = Esquema.objects.get(nome=q.nome_esquema)
            command = "create schema %s" % schema_name
            executar_comando(command)
            trocar_esquema(schema_name)
            executar_comando(e.criacao)
            result = comparar_respostas(answer, q.resposta_gabarito)
            u = Usuario.objects.get(login=request.user)
            i = Instancia()
            i.nome_esquema = e
            i.nome = schema_name
            i.login_usuario = u
            i.dt_criacao = datetime.now()
            i.save()
        # Armazenar a tentativa do aluno
        u = Usuario.objects.get(login=login)
        r = Resposta()
        r.login_usuario = u
        r.resposta = answer
        r.id_questao = q
        r.dt_resposta = datetime.now()
        if result:
            r.dt_acerto = r.dt_resposta
        r.save()
        # Obter todas as respostas anteriores
        l = ListaExercicio.objects.get(id=exercicio_id)
        questions = l.questao_set.all()
        dict = {}
        for q in questions:
            answers = q.resposta_set.all()
            if answers:
                aux = answers.filter(login_usuario=login)
                max_id = aux.aggregate(Max('id'))
                if aux.filter(id=max_id['id__max']):
                    a = aux.get(id=max_id['id__max'])
                    if a.dt_acerto is None:
                        correto = False
                    else:
                        correto = True
                    dict[q.id] = [a.resposta, correto]
        context_dict = {
            'answer': result,
            'answers': dict,
        }
        return show(request, exercicio_id, context_dict)


def comparar_respostas(resposta_aluno, resposta_gabarito):
    result = False
    cursor = connection.cursor()
    try:
        cursor.execute(resposta_gabarito)
        correct_answer = cursor.fetchall()
        cursor.execute(resposta_aluno)
        user_answer = cursor.fetchall()
        if user_answer == correct_answer:
            result = True
        else:
            result = False
        cursor.execute("set search_path to public")
        transaction.commit_unless_managed()
        cursor.close()
    except DatabaseError:
        connection._rollback()
        trocar_esquema('public')
    finally:
        return result


def trocar_esquema(nome_esquema):
    cursor = connection.cursor()
    command = "set search_path to %s" % nome_esquema
    cursor.execute(command)
    transaction.commit_unless_managed()
    cursor.close()


def executar_comando(sql):
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        transaction.commit_unless_managed()
        cursor.close()
    except DatabaseError:
        connection._rollback()
        trocar_esquema('public')