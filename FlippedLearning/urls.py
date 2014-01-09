from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FlippedLearning.views.home', name='home'),
    # url(r'^FlippedLearning/', include('FlippedLearning.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Login Page
    url(r'^$', 'database_app.views.usuario.login', name='login'),

    # Welcome Page
    url(r'^inicio/', 'database_app.views.usuario.inicio', name='inicio'),

    # Forum Page
    url(r'^forum/', 'database_app.views.forum.index', name='forum'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)