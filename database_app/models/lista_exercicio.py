from __future__ import unicode_literals
from django.db import models


class ListaExercicio(models.Model):
    descricao = models.TextField(max_length=1024, blank=True)
    dt_liberada = models.DateTimeField()

    def __unicode__(self):
        return self.descricao

    class Meta:
        db_table = 'lista_exercicio'
        verbose_name_plural = 'Listas de Exercicios'