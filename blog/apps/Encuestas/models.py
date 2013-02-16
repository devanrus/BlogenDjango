from django.db import models

class Preguntas (models.Model):
    pregunta = models.CharField(max_length=100)
    fecha = models.DateTimeField("Fecha de creacion")
    
    def __unicode__(self):
        return self.pregunta
    
class Opciones (models.Model):
    nompreg = models.ForeignKey(Preguntas)
    opciones = models.CharField(max_length=100)
    numvotos = models.IntegerField()
    
    def __unicode__ (self):
        return self.opciones

