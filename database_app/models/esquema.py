from __future__ import unicode_literals
from django.db import models


class Esquema(models.Model):
    nome = models.CharField(primary_key=True, max_length=50)
    criacao = models.TextField(max_length=4096)

    def __unicode__(self):
        return self.nome

    class Meta:
        db_table = 'esquema'