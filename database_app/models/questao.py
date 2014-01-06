from __future__ import unicode_literals
from django.db import models
from lista_exercicio import ListaExercicio
from usuario import Usuario
from esquema import Esquema


class Questao(models.Model):
    id_exercicio = models.ForeignKey(ListaExercicio, db_column='id_exercicio')
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')
    nome_esquema = models.ForeignKey(Esquema, db_column='nome_esquema', blank=True, null=True)
    pergunta = models.TextField(max_length=1024)
    resposta_gabarito = models.TextField(max_length=1024, db_column='resposta')

    def __unicode__(self):
        return self.pergunta;

    class Meta:
        db_table = 'questao'
        verbose_name_plural = 'Questoes'