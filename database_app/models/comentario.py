__author__ = 'jpedro'

from django.db import models

class Comentario(models.Model):
    dt_criacao = models.DateTimeField(auto_now_add=True)
    resposta = models.TextField(max_length=1024, null=False, blank=False)

    class Meta:
        db_table = 'comentario'
        app_label = 'database_app'
        verbose_name = 'Comentario'