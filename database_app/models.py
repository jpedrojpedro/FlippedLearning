from __future__ import unicode_literals

from django.db import models


class Assunto(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'assunto'


class AssuntoDuvida(models.Model):
    id_assunto = models.ForeignKey(Assunto, db_column='id_assunto')
    id_duvida = models.ForeignKey('Duvida', db_column='id_duvida')

    class Meta:
        db_table = 'assunto_duvida'
        verbose_name_plural = 'Assuntos Duvidas'


class AssuntoListaExercicio(models.Model):
    id_assunto = models.ForeignKey(Assunto, db_column='id_assunto')
    id_exercicio = models.ForeignKey('ListaExercicio', db_column='id_exercicio')

    class Meta:
        db_table = 'assunto_lista_exercicio'
        verbose_name_plural = 'Assuntos Listas de Exercicios'


class Comentario(models.Model):
    id_duvida = models.ForeignKey('Duvida', db_column='id_duvida')
    login_usuario = models.ForeignKey('Usuario', db_column='login_usuario')
    texto_comentario = models.CharField(max_length=1024)
    dt_comentario = models.DateTimeField()

    class Meta:
        db_table = 'comentario'


class Duvida(models.Model):
    id_assunto = models.ForeignKey(Assunto, db_column='id_assunto')
    login_usuario = models.ForeignKey('Usuario', db_column='login_usuario')
    id_questao = models.ForeignKey('Questao', db_column='id_questao', blank=True, null=True)
    pergunta = models.CharField(max_length=1024)
    dt_duvida = models.DateTimeField()

    class Meta:
        db_table = 'duvida'


class Esquema(models.Model):
    nome = models.CharField(primary_key=True, max_length=50)
    criacao = models.CharField(max_length=4096)

    class Meta:
        db_table = 'esquema'


class Instancia(models.Model):
    nome = models.CharField(primary_key=True, max_length=50)
    nome_esquema = models.ForeignKey(Esquema, db_column='nome_esquema')
    login_usuario = models.ForeignKey('Usuario', db_column='login_usuario')
    dt_criacao = models.DateTimeField()

    class Meta:
        db_table = 'instancia'


class ListaExercicio(models.Model):
    id_assunto = models.ForeignKey(Assunto, db_column='id_assunto')
    descricao = models.CharField(max_length=1024, blank=True)
    dt_liberada = models.DateTimeField()

    class Meta:
        db_table = 'lista_exercicio'
        verbose_name_plural = 'Listas de Exercicios'


class Modificacao(models.Model):
    nome_instancia = models.ForeignKey(Instancia, db_column='nome_instancia')
    login_usuario = models.ForeignKey('Usuario', db_column='login_usuario')
    dt_modificacao = models.DateTimeField()
    comando = models.CharField(max_length=1024)

    class Meta:
        db_table = 'modificacao'
        verbose_name_plural = 'Modificacoes'


class Questao(models.Model):
    id_exercicio = models.ForeignKey(ListaExercicio, db_column='id_exercicio')
    login_usuario = models.ForeignKey('Usuario', db_column='login_usuario')
    nome_esquema = models.ForeignKey(Esquema, db_column='nome_esquema', blank=True, null=True)
    pergunta = models.CharField(max_length=1024)
    resposta_gabarito = models.CharField(max_length=1024, db_column='resposta')

    class Meta:
        db_table = 'questao'
        verbose_name_plural = 'Questoes'


class Resposta(models.Model):
    id_questao = models.ForeignKey(Questao, db_column='id_questao')
    login_usuario = models.ForeignKey('Usuario', db_column='login_usuario')
    dt_resposta = models.DateTimeField()
    dt_acerto = models.DateTimeField(blank=True, null=True)
    resposta = models.CharField(max_length=1024)

    class Meta:
        db_table = 'resposta'


class Usuario(models.Model):
    login = models.CharField(primary_key=True, max_length=20)
    senha = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    professor = models.TextField() # This field type is a guess.

    class Meta:
        db_table = 'usuario'


class UsuarioModeraComentario(models.Model):
    login_moderador = models.ForeignKey(Usuario, db_column='login_moderador')
    id_comentario = models.ForeignKey(Comentario, db_column='id_comentario')
    justificativa = models.CharField(max_length=1024)
    dt_cancelamento = models.DateTimeField()

    class Meta:
        db_table = 'usuario_modera_comentario'
        verbose_name_plural = 'Usuarios Moderam Comentarios'


class UsuarioModeraDuvida(models.Model):
    login_moderador = models.ForeignKey(Usuario, db_column='login_moderador')
    id_duvida = models.ForeignKey(Duvida, db_column='id_duvida')
    justificativa = models.CharField(max_length=1024)
    dt_cancelamento = models.DateTimeField()

    class Meta:
        db_table = 'usuario_modera_duvida'
        verbose_name_plural = 'Usuarios Moderam Duvidas'


class Visualizacao(models.Model):
    nome_instancia = models.ForeignKey(Instancia, db_column='nome_instancia')
    login_usuario = models.ForeignKey(Usuario, db_column='login_usuario')

    class Meta:
        db_table = 'visualizacao'
        verbose_name_plural = 'Visualizacoes'