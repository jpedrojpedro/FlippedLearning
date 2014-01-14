from __future__ import unicode_literals
from django.db import models
from usuario import Usuario
from duvida import Duvida


class UsuarioModeraDuvida(models.Model):
    login_moderador = models.ForeignKey(Usuario, db_column='login_moderador')
    id_duvida = models.ForeignKey(Duvida, db_column='id_duvida')
    justificativa = models.CharField(max_length=1024)
    dt_cancelamento = models.DateTimeField()

    class Meta:
        db_table = 'usuario_modera_duvida'
        verbose_name_plural = 'Usuarios Moderam Duvidas'
        app_label = 'database_app'
        unique_together = (("login_moderador", "id_duvida"),)