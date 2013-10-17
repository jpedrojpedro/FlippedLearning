__author__ = 'jpedro'

from django.contrib import admin

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id',)