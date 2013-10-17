__author__ = 'jpedro'

from django.db import models

class Disciplina(models.Model):
    codigo = models.CharField(max_length=7, primary_key=True)
    nome = models.CharField(max_length=100, blank=False, null=False)
    ementa = models.TextField(max_length=1024, blank=True, null=True)