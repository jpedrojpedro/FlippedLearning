# coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import User
from django import forms
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


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
    senha = forms.CharField(widget=forms.PasswordInput(render_value='*'))


class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioForm

    def save_model(self, request, obj, form, change):
        u, created = User.objects.get_or_create(username=obj.login)
        u.username = obj.login
        u.password = obj.senha
        u.email = obj.email
        u.first_name = obj.nome
        if obj.professor == '1':
            u.is_staff = True
            u.is_superuser = True
            u.is_active = True
        else:
            u.is_staff = False
            u.is_superuser = False
            u.is_active = False
        u.save()
        obj.save()


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
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(UsuarioModeraComentario)
admin.site.register(UsuarioModeraDuvida)
admin.site.register(Visualizacao)