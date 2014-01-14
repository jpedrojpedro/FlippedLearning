# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection, transaction
from database_app.models.questao import Questao
from database_app.models.instancia import Instancia
from database_app.models.esquema import Esquema

@login_required
def verificar(request, exercicio_id, questao_id):
    if request.POST:
        r = request.POST['resposta']
        # Obtendo a questão respondida
        q = Questao.objects.get(id=questao_id)
        schema_name = "%s_%s" % (q.nome_esquema, request.user)
        # Verificando se a instancia existe
        i = Instancia.objects.filter(nome_esquema=q.nome_esquema, login_usuario=request.user)
        # Caso em que a instancia existe
        if i:
            cursor = connection.cursor()
            command = "set search_path to %s" % schema_name
            cursor.execute(command)
            transaction.commit_unless_managed()
            # Trecho igual -- Otimizar
            cursor.execute(q.resposta_gabarito)
            answer = cursor.fetchall()
            cursor.execute(r)
            answer_user = cursor.fetchall()
            if answer == answer_user:
                result = True
            else:
                result = False
            cursor.execute("set search_path to public")
            transaction.commit_unless_managed()
        # Caso em que a instancia não existe -- Salvar na tabela!
        else:
            e = Esquema.objects.get(nome=q.nome_esquema)
            cursor = connection.cursor()
            command = "create schema %s" % schema_name
            cursor.execute(command)
            transaction.commit_unless_managed()
            command = "set search_path to %s" % schema_name
            cursor.execute(command)
            transaction.commit_unless_managed()
            cursor.execute(e.criacao)
            transaction.commit_unless_managed()
            # Trecho igual -- Otimizar
            cursor.execute(q.resposta_gabarito)
            answer = cursor.fetchall()
            cursor.execute(r)
            answer_user = cursor.fetchall()
            if answer == answer_user:
                result = True
            else:
                result = False
            cursor.execute("set search_path to public")
            transaction.commit_unless_managed()
        template = loader.get_template("question_page.html")
        context = RequestContext(request, {
            'answer': result,
        })
        return HttpResponse(template.render(context))