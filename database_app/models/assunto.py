from __future__ import unicode_literals
from django.db import models


class Assunto(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'assunto'
        app_label = 'database_app'