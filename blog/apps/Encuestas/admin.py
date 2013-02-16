'''
Created on 31/01/2013

@author: Rams
'''
from blog.apps.Encuestas.models import Preguntas, Opciones
from django.contrib import admin

admin.site.register(Preguntas)
admin.site.register(Opciones)
