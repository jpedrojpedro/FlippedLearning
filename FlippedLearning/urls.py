from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FlippedLearning.views.home', name='home'),
    # url(r'^FlippedLearning/', include('FlippedLearning.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Login Page
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login_page.html'}, name='login'),

    # Logout Page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    # Welcome Page
    url(r'^inicio/', 'database_app.views.usuario.inicio', name='inicio'),
    url(r'^$', 'database_app.views.usuario.inicio', name='home'),

    url(r'^inicio/', 'database_app.views.usuario.inicio', name='inicio'),

    # Forum Page
    url(r'^forum/$', 'database_app.views.forum.index', name='forum'),

    # Forum Page :: Busca
    url(r'^forum/busca/$', 'database_app.views.forum.search', name='busca'),

    # Forum Page :: Adicionar Comentario
    url(r'^comentario/add/$', 'database_app.views.comentario.add', name='adicionar_comentario'),

    # Forum Page :: Adicionar Duvida
    url(r'^duvida/add/$', 'database_app.views.duvida.add', name='adicionar_duvida'),

    # Exercise Page
    url(r'^exercicio/$', 'database_app.views.exercicio.list_all', name='exercicio'),

    # Question Page :: Abrir Exercicio
    url(r'^exercicio/(?P<exercicio_id>\d+)/$', 'database_app.views.exercicio.show', name='abrir_exercicio'),

    # Question Page :: Verificar Questao
    url(r'^exercicio/(?P<exercicio_id>\d+)/questao/(?P<questao_id>\d+)$',
        'database_app.views.questao.verificar', name='verificar_questao'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Static Files
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
