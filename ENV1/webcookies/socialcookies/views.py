from django.shortcuts import render
from django.http import HttpResponse

from djangomako.shortcuts import render_to_response, render_to_string

import os

# Create your views here.

#def hola(request):
	#return HttpResponse("Hola")
	
ficheros = os.listdir('/home/francisco/Documentos/Facultad/SocialCookies/ENV1/webcookies/socialcookies/static/socialcookies/bootstrap/img-slider') 

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
	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
    	'seccion': 'contacto',
    	'fich':ficheros})

