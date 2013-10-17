__author__ = 'jpedro'

from django.db import models

class Instancia(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)