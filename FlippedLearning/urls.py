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

    # Boas Vindas
    url(r'^$', 'database_app.boas_vindas.views.index', name='inicio'),

    # Usuario
    url(r'^usuario$', 'database_app.usuario.views.index', name='usuario'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)