from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.apps.Encuestas.models import Preguntas
from blog.apps.noticias.models import Noticias
from blog.apps.noticias.models import Categoria

def index (request):
	obtiene = Preguntas.objects.all().order_by ('-fecha')[:5]
	obtienenoticias = Noticias.objects.all().order_by('-fecha')[:4]
	return render_to_response ('index.html',{'ultimasnoticias':obtienenoticias,'ultimaspreg':obtiene}, context_instance = RequestContext(request))

def contacto (request) :
	return render_to_response ('contacto.html', context_instance = RequestContext(request))

