from __future__ import unicode_literals
from django.db import models
from instancia import Instancia
from usuario import Usuario


class Visualizacao(models.Model):
    nome_instancia = models.ForeignKey(Instancia, db_column='nome_instancia', primary_key=True)
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario', primary_key=True)

    class Meta:
        db_table = 'visualizacao'
        verbose_name_plural = 'Visualizacoes'
        app_label = 'database_app'