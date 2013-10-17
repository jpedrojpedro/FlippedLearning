__author__ = 'jpedro'

from django.db import models

class Duvida(models.Model):
    assunto = models.CharField(max_length=50, null=True, blank=True)
    pergunta = models.CharField(max_length=1024, null=False, blank=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)