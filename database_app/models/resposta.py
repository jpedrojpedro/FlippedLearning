from __future__ import unicode_literals
from django.db import models
from questao import Questao
from usuario import Usuario


class Resposta(models.Model):
    id_questao = models.ForeignKey(Questao, db_column='id_questao')
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')
    dt_resposta = models.DateTimeField()
    dt_acerto = models.DateTimeField(blank=True, null=True)
    resposta = models.CharField(max_length=1024)

    class Meta:
        db_table = 'resposta'