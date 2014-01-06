from __future__ import unicode_literals
from django.db import models


class Usuario(models.Model):
    login = models.CharField(primary_key=True, max_length=20)
    senha = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    professor = models.CharField(choices=(('1', 'Sim'), ('0', 'Nao')), default='0', max_length=1)

    def __unicode__(self):
        return self.login

    class Meta:
        db_table = 'usuario'