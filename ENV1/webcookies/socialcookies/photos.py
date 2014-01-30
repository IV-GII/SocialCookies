# -*- coding: utf-8 -*- 

from instagram import client, subscriptions
#from web.contrib.template import render_mako
from django.http import HttpResponse,  HttpResponseRedirect
from djangomako.shortcuts import render_to_response, render_to_string

import os

ficheros = os.listdir('./socialcookies/static/socialcookies/bootstrap/img-slider') 
#ficheros = os.listdir('/Users/anabelen/Documents/GitHub/SocialCookies/ENV1/webcookies/socialcookies/static/socialcookies/bootstrap/img-slider') 

CONFIG = {
	'client_id': 		'acb74f518fad45e18df287b8da777717',
    'client_secret': 	'093fa01b5aa84d15b1eb58ac5a58b4f8',
    'redirect_uri': 	'http://127.0.0.1:8000/socialcookies/oauth_callback'
    
    #'client_id': 		'28aecdf96ffd477297887aad3fcf624e',
    #'client_secret': 	'3b6ffb3a32674b63acb1c0dcbc0e1912',
    #'redirect_uri': 	'http://socialcookies.cloudapp.net/socialcookies/oauth_callback'
}

count = 24

unauthenticated_api = client.InstagramAPI(**CONFIG)

def process_tag_update(update):
    print update

reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)


def instagram(request):

    #return HttpResponse("hola")
    # try:

    url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        
    return HttpResponseRedirect(url)
    #     return '<a href="%s">Connect with Instagram</a>' % url
    # except Exception, e:
    #     print e


def on_callback(request):
    


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
        {'path': '/static/socialcookies/bootstrap/',
        'seccion': 'instagram',
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


