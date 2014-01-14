# coding=utf-8

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection
from database_app.models.questao import Questao
from database_app.models.instancia import Instancia

@login_required
def verificar(request, exercicio_id, questao_id):
    if request.POST:
        r = request.POST['resposta']
        # Obtendo a questão respondida
        q = Questao.objects.get(id=questao_id)
        schema_name = "%s_%s" % (q.nome_esquema, request.user)
        # Verificando se a instancia existe
        i = Instancia.objects.get(nome_esquema=schema_name)
        # Caso em que a instancia existe
        if i:
            cursor = connection.cursor()
            cursor.execute("set search_path to %s", [schema_name])
            cursor.execute(q.resposta_gabarito)
            answer = cursor.fetchone()
            cursor.execute(r)
            answer_user = cursor.fetchone()
            if answer == answer_user:
                result = True
            else:
                result = False