import bottle
from bottle import route, post, run, request
from instagram import client, subscriptions

bottle.debug(True)

CONFIG = {
    'client_id': '28aecdf96ffd477297887aad3fcf624e',
    'client_secret': '3b6ffb3a32674b63acb1c0dcbc0e1912',
    'redirect_uri': 'http://localhost:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

def process_tag_update(update):
    print update

reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)

@route('/')
def home():
    try:
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
        return '<a href="%s">Connect with Instagram</a>' % url
    except Exception, e:
        print e

@route('/oauth_callback')
def on_callback():
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
            
            photos.append('<img src="%s"  onClick="imgFunction(this)" />' % media.images['thumbnail'].url)

        photos = ''.join(photos)

        #Descargamos las imagenes
        popular_media = api.media_popular(6)
        #Guardamos las imagenes
        popular = []
        for media in popular_media:
            popular.append('<img src="%s"/>' % media.images['thumbnail'].url)
        popular = ''.join(popular)
        
        return """
        <script type='text/javascript'>
        function imgFunction(objeto){
        	if(objeto.style.opacity==1){
		    	objeto.style.opacity=0.4;
        	}
        	else{
        		objeto.style.opacity=1;
        	}
		}
		</script>
        Photos from Instagram <br>""" + photos + "<br><br> Top photos from Instagram <br>" + popular
       
    except Exception, e:
        print e

@route('/realtime_callback')
@post('/realtime_callback')

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

run(host='localhost', port=8515, reloader=True)