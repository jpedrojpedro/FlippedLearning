__author__ = 'jpedro'

from django.db import models

class Modificacao(models.Model):
    dt_modificacao = models.DateTimeField(auto_now_add=True)
    comando = models.TextField(max_length=1024, null=False, blank=False)