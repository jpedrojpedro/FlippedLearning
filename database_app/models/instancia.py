from __future__ import unicode_literals
from django.db import models
from esquema import Esquema
from usuario import Usuario


class Instancia(models.Model):
    nome = models.CharField(primary_key=True, max_length=50)
    nome_esquema = models.ForeignKey(Esquema, db_column='nome_esquema')
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')
    dt_criacao = models.DateTimeField()

    class Meta:
        db_table = 'instancia'
        app_label = 'database_app'