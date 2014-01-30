from django.shortcuts import render
from django.http import HttpResponse
from socialcookies.forms import ContactForm
from djangomako.shortcuts import render_to_response, render_to_string
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.mail import send_mail
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

import photos

import os


# Create your views here.

#def hola(request):
	#return HttpResponse("Hola")
	
ficheros = os.listdir('/Users/anabelen/Documents/GitHub/SocialCookies/ENV1/webcookies/socialcookies/static/socialcookies/bootstrap/img-slider') 

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

    	
def mandaCorreo(titulo, contenido):

	#fromaddr = "socialcookies@gmail.com"
	#toaddr   = "socialcookies@gmail.com"

	#msg = MIMEMultipart ()
	#msg['From']    = fromaddr
	#msg['To']         = toaddr
	#msg['Subject'] = titulo

	#body = contenido
	#msg.attach (MIMEText (body, 'plain'))

	#server = smtplib.SMTP ('smtp.gmail.com', 587)
	#server.ehlo ()
	#server.starttls ()   # Para conexion cifrada
	#server.ehlo ()
	#server.login ("socialcookies", "IVsocialcookies")
	#text = msg.as_string ()
	#server.sendmail(fromaddr, toaddr, text)
	
	email = EmailMessage(titulo, contenido, to=['socialcookiesiv@gmail.com'])
	email.send()


def contacto(request):
	if request.method=='POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje de contacto desde \"Social Cookies\"'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a : ' + formulario.cleaned_data['correo']
			mandaCorreo(titulo, contenido)
			return HttpResponseRedirect('/socialcookies')
	else:
		formulario = ContactForm()

	return render_to_response('index.html',
		{'path':'/static/socialcookies/bootstrap/',
		'seccion': 'contacto',
		'formulario':formulario,
		"csrftoken": csrf(request)["csrf_token"],
		'fich':ficheros})
    	
#def pedido(request):
#	if request.method=='POST':
#		formu = PedidoForm(request.POST)
#		if formu.is_valid():
#			titulo = 'Mensaje de contacto desde \"Social Cookies\"'
#			contenido = 'Cliente: ' + formu.cleaned_data['nombre'] + "\n"
#			contenido += 'Direccion' + formu.cleaned_data['direccion'] + "\n"
#			contenido += 'Telefono' + formu.cleaned_data['telefono'] + "\n"
#			contenido += 'Correo' + formu.cleaned_data['correo']
#			mandaCorreo(titulo, contenido)
#			return HttpResponseRedirect('/socialcookies')
#	else:
#		formu = PedidoForm()
#
#	return render_to_response('index.html',
#		{'path':'/static/socialcookies/bootstrap/',
#		'seccion': 'contacto',
#		'formu':formu,
#		"csrftoken": csrf(request)["csrf_token"],
#		'fich':ficheros})
