from blog.apps.Encuestas.models import Preguntas
from django.http import HttpResponse

def index (request):
    ultimas_preguntas = Preguntas.objects.all().order_by('-fecha') [:2]
    output = ', '.join([obj.preguntas for obj in ultimas_preguntas])
    return HttpResponse (output)

def detalle (request,Preguntas_id):
    return HttpResponse ("Estas en la pregunta con id: %s" %Preguntas_id)

def resultado (request,Preguntas_id):
    return HttpResponse ("El resultado de la pregunta: %s" %Preguntas_id)

def votos (request,Preguntas_id):
    return HttpResponse ("EL voto es para: %s"%Preguntas_id)
