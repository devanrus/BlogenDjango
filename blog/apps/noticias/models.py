from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)
	fechacreacion = models.DateField()

	def __unicode__(self):
		return self.nombre

class Noticias (models.Model):
	cat = models.ForeignKey(Categoria)
	titulo = models.CharField(max_length=30)
	contenido = models.TextField(max_length=5000)
	fecha = models.DateTimeField('Fecha de Publicacion')
	imagen = models.ImageField (upload_to='images', verbose_name ='Imagen')

	def __unicode__ (self):
		return self.titulo






