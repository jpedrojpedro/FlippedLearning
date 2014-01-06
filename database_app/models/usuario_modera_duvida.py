from __future__ import unicode_literals
from django.db import models
from usuario import Usuario
from duvida import Duvida


class UsuarioModeraDuvida(models.Model):
    login_moderador = models.ForeignKey(Usuario, db_column='login_moderador', primary_key=True)
    id_duvida = models.ForeignKey(Duvida, db_column='id_duvida', primary_key=True)
    justificativa = models.CharField(max_length=1024)
    dt_cancelamento = models.DateTimeField()

    class Meta:
        db_table = 'usuario_modera_duvida'
        verbose_name_plural = 'Usuarios Moderam Duvidas'