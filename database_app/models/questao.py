__author__ = 'jpedro'

from django.db import models

class Questao(models.Model):
    pergunta = models.TextField(max_length=1024, null=False, blank=False)
    resposta = models.TextField(max_length=1024, null=False, blank=False)