# -*- coding: utf-8 -*- 

# Copyright (C) 2014  SocialCookies @IV/GII

# @anaprados @oskyar @torresj @josemlp91
# @franciscomanuel @rogegg  @pedroag  @melero90

# Aplicacion web, para gestionar pedidos de galletas,
# con fotos de Instagram y Twitter. 

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.



from instagram import client, subscriptions
from django.core.context_processors import csrf
#from web.contrib.template import render_mako
from django.http import HttpResponse,  HttpResponseRedirect
from djangomako.shortcuts import render_to_response, render_to_string
from socialcookies.forms import fotosPedido
import os
from conf import *   #conf.py es secreto

ficheros = os.listdir('./socialcookies/static/img-slider') 

count = 24

unauthenticated_api = client.InstagramAPI(**CONFIG)

def process_tag_update(update):
    print update

reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)


def instagram(request):

    
    try:

        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        return HttpResponseRedirect(url)

    except Exception, e:
        print e


def on_callback(request):
    
    if request.method=='POST':
        formu = fotosPedido(request.POST)
        

        if formu.is_valid():
            print formulario2.cleaned_data['hidden_field0']
            return render_to_response('index.html',
        {'path':'/static/',
        'seccion': 'contacto',
        'formulario':formu,
        "csrftoken": csrf(request)["csrf_token"],
        'fich':ficheros})

    else:
        formu = fotosPedido()
        code = request.GET.get("code")

        if not code:
            return 'Missing code'
        try:
            access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
            
            if not access_token:
                return 'Could not get access token'
            
            api = client.InstagramAPI(access_token=access_token)
            
            #Descargamos las imagenes
            recent_media, next = api.user_recent_media(count)
            #Guardamos las imagenes
            usuario = []
            	#photos
            	#profile
            	#name

            for media in recent_media:
         									 #'standard_resolution'
    		    usuario.append([ media.images['low_resolution'].url,
    						 	 media.user.profile_picture,
    		    			 	 media.user.full_name ])
    		   		
            #Descargamos las imagenes
            popular_media = api.media_popular(count)
            print len(popular_media)
            #Guardamos las imagenes
            popular = []
            	#photos
            	#profile
            	#name

            for media in popular_media:
            								 #'standard_resolution'
                popular.append([ media.images['low_resolution'].url,
    						 	 media.user.profile_picture,
    		    			 	 media.user.full_name ])
                

    		#Enviamos las imagenes al archivo html
            return render_to_response('index.html',
            {'path': '/static/',
            'seccion': 'instagram',
            'formulario':formu,
            "csrftoken": csrf(request)["csrf_token"],
            'usuario': usuario,
            'popular': popular,
        	'fich':ficheros
            
            })
           
        except Exception, e:
            print e

def on_realtime_callback():
    mode = request.GET.get("hub.mode")
    challenge = request.GET.get("hub.challenge")
    verify_token = request.GET.get("hub.verify_token")
    if challenge: 
        return challenge
    else:
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body.read()
        try:
            reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            print "Signature mismatch"


