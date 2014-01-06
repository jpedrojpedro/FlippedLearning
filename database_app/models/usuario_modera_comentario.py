from __future__ import unicode_literals
from django.db import models
from usuario import Usuario
from comentario import Comentario


class UsuarioModeraComentario(models.Model):
    login_moderador = models.ForeignKey(Usuario, db_column='login_moderador', primary_key=True)
    id_comentario = models.ForeignKey(Comentario, db_column='id_comentario', primary_key=True)
    justificativa = models.CharField(max_length=1024)
    dt_cancelamento = models.DateTimeField()

    class Meta:
        db_table = 'usuario_modera_comentario'
        verbose_name_plural = 'Usuarios Moderam Comentarios'