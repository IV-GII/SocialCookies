from django.shortcuts import render
from django.http import HttpResponse
from socialcookies.forms import ContactForm
from djangomako.shortcuts import render_to_response, render_to_string

import os

# Create your views here.

#def hola(request):
	#return HttpResponse("Hola")
	
ficheros = os.listdir('/home/oskyar/proyectosGit/SocialCookies/ENV1/webcookies/socialcookies/static/socialcookies/bootstrap/img-slider') 

def index(request):
    return render_to_response('index.html',
    	{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'index',
    	'fich':ficheros})

def twitter(request):
	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'twitter',
    	'fich':ficheros})

def instagram(request):
	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'instagram',
    	'fich':ficheros})

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
    	'formulario':formulario,
    	'fich':ficheros})

