from __future__ import unicode_literals
from django.db import models
from duvida import Duvida
from usuario import Usuario


class Comentario(models.Model):
    id_duvida = models.ForeignKey(Duvida, db_column='id_duvida', blank=False, null=False)
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')
    texto_comentario = models.TextField(max_length=1024)
    dt_comentario = models.DateTimeField()

    class Meta:
        db_table = 'comentario'
        app_label = 'database_app'