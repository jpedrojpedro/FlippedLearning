__author__ = 'jpedro'

from django.contrib import admin

#models
from database_app.models.comentario import Comentario
from database_app.models.disciplina import Disciplina
from database_app.models.duvida import Duvida
from database_app.models.esquema import Esquema
from database_app.models.exercicio import Exercicio
from database_app.models.forum import Forum
from database_app.models.instancia import Instancia
from database_app.models.modificacao import Modificacao
from database_app.models.usuario import Usuario

#admin
from database_app.admin.comentario import ComentarioAdmin

admin.site.register(Comentario, ComentarioAdmin)