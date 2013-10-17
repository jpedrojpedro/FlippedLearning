__author__ = 'jpedro'

from django.db import models

class Forum(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=1024, null=True, blank=True)