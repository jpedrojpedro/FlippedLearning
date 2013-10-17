__author__ = 'jpedro'

from django.db import models

class Esquema(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    comando_criacao = models.TextField(max_length=4096, null=False, blank=False)