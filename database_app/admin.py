# coding=utf-8

from django.contrib import admin
from models.assunto import Assunto
from models.assunto_duvida import AssuntoDuvida
from models.assunto_lista_exercicio import AssuntoListaExercicio
from models.comentario import Comentario
from models.duvida import Duvida
from models.esquema import Esquema
from models.instancia import Instancia
from models.lista_exercicio import ListaExercicio
from models.modificacao import Modificacao
from models.questao import Questao
from models.resposta import Resposta
from models.usuario import Usuario
from models.usuario_modera_comentario import UsuarioModeraComentario
from models.usuario_modera_duvida import UsuarioModeraDuvida
from models.visualizacao import Visualizacao


admin.site.register(Assunto)
admin.site.register(AssuntoDuvida)
admin.site.register(AssuntoListaExercicio)
admin.site.register(Comentario)
admin.site.register(Duvida)
admin.site.register(Esquema)
admin.site.register(Instancia)
admin.site.register(ListaExercicio)
admin.site.register(Modificacao)
admin.site.register(Questao)
admin.site.register(Resposta)
admin.site.register(Usuario)
admin.site.register(UsuarioModeraComentario)
admin.site.register(UsuarioModeraDuvida)
admin.site.register(Visualizacao)