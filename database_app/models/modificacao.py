from __future__ import unicode_literals
from django.db import models
from instancia import Instancia
from usuario import Usuario


class Modificacao(models.Model):
    nome_instancia = models.ForeignKey(Instancia, db_column='nome_instancia')
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')
    dt_modificacao = models.DateTimeField()
    comando = models.CharField(max_length=1024)

    class Meta:
        db_table = 'modificacao'
        verbose_name_plural = 'Modificacoes'