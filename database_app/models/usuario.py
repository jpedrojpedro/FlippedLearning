__author__ = 'jpedro'

from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=20, primary_key=True)
    senha = models.CharField(max_length=15, blank=False, null=False)
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    professor = models.BooleanField(default=False)