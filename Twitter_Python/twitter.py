import tweepy
import web
from web.contrib.template import render_mako
from web import form

web.config.debug=False

consumer_key = 'acisTloOHSws1UA289etVw'
consumer_secret = 'b9eVS9CeFxIFx3jIwKkeeQPfsO3hlrAdWNOfIItQEgU'
access_token = '2308079432-cDmExMexRNNwAEvIUdrtKQFXgfIA1vQPeM4mLRC'
access_token_secret = 'eUFjHJf3Wbqzo6NKxJRHE0HapuzNBzLynA8nOTOPygqis'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

urls=(
	'/', 'Home',
	'/Mostrar','Mostrar',
	'/Salida','Salida',	
)

app=web.application(urls, globals())

render=render_mako(directories=['templates'],input_encoding='utf-8',output_encoding='utf-8')

formulario=form.Form(
	form.Textbox("busqueda", form.notnull, description="busqueda"),
	form.Button("Enviar"),
)


class Home:

	def GET(self):
		f=formulario()
		return render.index(formu=f.render())

class Mostrar:

	def POST(self):
		entrada=web.input()
		busq=entrada.busqueda
		
		tuits=[]
		for tweet in tweepy.Cursor(api.search,q=busq,count=100,result_type="photo",include_entities=True).items(100):
    			if 'media' in tweet.entities:
        			for image in  tweet.entities['media']:
					tuits.append("<img src='%s'  onClick='imgFunction(this, \"%s\")' />" % (image['media_url'],image['media_url']))
		tuits = ''.join(tuits)
		
		return """
        	<script type='text/javascript'>
        	
			var elegidos = new Array();
        	
        	function imgFunction(objeto, url){
        		        	
        		if(objeto.style.opacity==1){
			    	objeto.style.opacity=0.4;
			    	elegidos.push(url);
			    	console.log(elegidos.valueOf(elegidos.length-1));
        		}
        		else{
        			objeto.style.opacity=1;
        			indice = elegidos.indexOf(url);
        			if(indice!=-1)
        				elegidos.splice(indice,1);
        		}
        	}
			</script>
        	Photos from Twitter <br>""" + tuits
		
	

if __name__=="__main__":
	app.run()
