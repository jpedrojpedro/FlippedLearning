from __future__ import unicode_literals
from django.db import models
from usuario import Usuario
from questao import Questao


class Duvida(models.Model):
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')
    id_questao = models.ForeignKey(Questao, db_column='id_questao', blank=True, null=True)
    pergunta = models.CharField(max_length=1024)
    dt_duvida = models.DateTimeField()

    class Meta:
        db_table = 'duvida'