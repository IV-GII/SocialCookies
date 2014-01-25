from django.shortcuts import render
from django.http import HttpResponse

from djangomako.shortcuts import render_to_response, render_to_string

# Create your views here.

#def hola(request):
	#return HttpResponse("Hola")

def index(request):
    return render_to_response('index.html',
    	{'path':'/static/socialcookies/bootstrap/'})
