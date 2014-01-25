# -*- coding: utf-8 -*- 

from instagram import client, subscriptions
from web.contrib.template import render_mako
from django.http import HttpResponse,  HttpResponseRedirect
from djangomako.shortcuts import render_to_response, render_to_string


CONFIG = {
    'client_id': '28aecdf96ffd477297887aad3fcf624e',
    'client_secret': '3b6ffb3a32674b63acb1c0dcbc0e1912',
    'redirect_uri': 'http://localhost:8000/socialcookies/oauth_callback'
}

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
        recent_media, next = api.user_recent_media(6)
        #Guardamos las imagenes
        photos = []

        for media in recent_media:

            
            photos.append(media.images['thumbnail'].url)


        #photos = ''.join(photos)

        #Descargamos las imagenes
        popular_media = api.media_popular(6)
        #Guardamos las imagenes
        popular = []
        for media in popular_media:

            popular.append(media.images['thumbnail'].url)

        #popular = ''.join(popular)
        
       # return render.plantilla(Titulo='Desarrollo de Aplicaciones para Internet', Subtitulo='RSS, Google Chart, Maps y Twitter',login=login,cate=cat,cateA=web.websafe(i.categoria),
       #         losPosts=losPosts, autor='Jose Miguel Lopez', reg=reg,log=log,user=user,error=False, vLink=vectorLink,vtS="",rss=rss)
        
        #return render.plantilla(photos=photos, popular=popular)



        return render_to_response('index.html',
        {'path': '/static/socialcookies/bootstrap/',
        'seccion': 'instagram',
        'photos': photos,
        'popular': popular
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


