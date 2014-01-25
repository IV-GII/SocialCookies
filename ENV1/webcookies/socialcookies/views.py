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
    	
def mandaCorreo(titulo, contenido):

	fromaddr = "socialcookies@hotmail.com"
	toaddr   = "socialcookies@hotmail.com"

	msg = MIMEMultipart ()
	msg['From']    = fromaddr
	msg['To']         = toaddr
	msg['Subject'] = titulo

	body = contenido
	msg.attach (MIMEText (body, 'plain'))

	server = smtplib.SMTP ('smtp.live.com', 25)
	server.ehlo ()
	server.starttls ()   # Para conexion cifrada
	server.ehlo ()
	server.login ("socialcookies", "IVgalletas")
	text = msg.as_string ()
	server.sendmail(fromaddr, toaddr, text)

def contacto(request):
	if request.method=='POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje de contacto desde \"Social Cookies\"'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a : ' #+ formulario.cleaned_data['correo']
			#correo = EmailMessage(titulo, contenido, to=['oskyar@gmail.com'])
			#correo.send()
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
    

    	


