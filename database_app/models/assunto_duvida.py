from __future__ import unicode_literals
from django.db import models
from assunto import Assunto
from duvida import Duvida


class AssuntoDuvida(models.Model):
    id_assunto = models.ForeignKey(Assunto, db_column='id_assunto')
    id_duvida = models.ForeignKey(Duvida, db_column='id_duvida')

    class Meta:
        db_table = 'assunto_duvida'
        verbose_name_plural = 'Assuntos Duvidas'
        app_label = 'database_app'
        unique_together = (("id_assunto", "id_duvida"),)