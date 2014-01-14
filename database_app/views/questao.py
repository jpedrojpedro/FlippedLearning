# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection, transaction
from database_app.models.questao import Questao
from database_app.models.instancia import Instancia
from database_app.models.esquema import Esquema
from database_app.models.usuario import Usuario
from datetime import datetime

@login_required
def verificar(request, exercicio_id, questao_id):
    if request.POST:
        r = request.POST['resposta']
        # Obtendo a questão respondida
        q = Questao.objects.get(id=questao_id)
        schema_name = "%s_%s" % (q.nome_esquema, request.user)
        login = "%s" % request.user
        # Verificando se a instancia existe
        i = Instancia.objects.filter(nome_esquema=q.nome_esquema, login_usuario=login)
        # Caso em que a instancia existe
        if i:
            trocar_esquema(schema_name)
            result = comparar_respostas(r, q.resposta_gabarito)
        # Caso em que a instancia não existe -- Salvar na tabela!
        else:
            e = Esquema.objects.get(nome=q.nome_esquema)
            command = "create schema %s" % schema_name
            executar_comando(command)
            trocar_esquema(schema_name)
            executar_comando(e.criacao)
            result = comparar_respostas(r, q.resposta_gabarito)
            u = Usuario.objects.get(login=request.user)
            i = Instancia()
            i.nome_esquema = e
            i.nome = schema_name
            i.login_usuario = u
            i.dt_criacao = datetime.now()
            i.save()
        template = loader.get_template("question_page.html")
        context = RequestContext(request, {
            'answer': result,
        })
        return HttpResponse(template.render(context))


def comparar_respostas(resposta_aluno, resposta_gabarito):
    cursor = connection.cursor()
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
    return result


def trocar_esquema(nome_esquema):
    cursor = connection.cursor()
    command = "set search_path to %s" % nome_esquema
    cursor.execute(command)
    transaction.commit_unless_managed()
    cursor.close()


def executar_comando(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    transaction.commit_unless_managed()
    cursor.close()