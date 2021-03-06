from __future__ import unicode_literals
from django.db import models
from assunto import Assunto
from lista_exercicio import ListaExercicio


class AssuntoListaExercicio(models.Model):
    id_assunto = models.ForeignKey(Assunto, db_column='id_assunto')
    id_exercicio = models.ForeignKey(ListaExercicio, db_column='id_exercicio')

    class Meta:
        db_table = 'assunto_lista_exercicio'
        verbose_name_plural = 'Assuntos Listas de Exercicios'
        app_label = 'database_app'
        unique_together = (("id_assunto", "id_exercicio"),)