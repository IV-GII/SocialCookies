from django.shortcuts import render
from django.http import HttpResponse
from socialcookies.forms import ContactForm
from djangomako.shortcuts import render_to_response, render_to_string

# Create your views here.

#def hola(request):
	#return HttpResponse("Hola")

def index(request):
    return render_to_response('index.html',
    	{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'index'})

def twitter(request):
	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'twitter'})

def instagram(request):
	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'instagram'})

def contacto(request):
	if request.method=='POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje de contacto desde \"Social Cookies\"'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a : ' + formulario.cleaned_data['correo']
			correo = EmailMEssage(titulo, contenido, to=['oskyar@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactForm()

	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'contacto',
    	'formulario':formulario})


