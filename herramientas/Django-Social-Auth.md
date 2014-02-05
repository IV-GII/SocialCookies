#Conociendo ```django-social-auth```
-------------------

Es un modulo de django que permite integrar muchísimas redes sociales a nuestras aplicaciones.

Amazon, Angel List, Appsfuel, Behance, Bitbucket, BrowserID, DISQUS, Douban, Dropbox, Evernote, ExactTarget, Facebook, Flickr, GitHub, Google
**Instagram** , LinkedIn, MSN Live,
Rdio, Readability, Reddit, Shopify, Skyrock, SoundCloud
Tumblr, **Twitter**, VK.com, Yahoo

Con lo cual el potencial que puede dar a nuestras aplicación es muy grande.

La documentación esta bastante bien y la podemos consultar en: [enlace documentacion django-social-auth](http://django-social-auth.readthedocs.org/en/latest/index.html#)


La conexiones con las redes sociales tiene una utilidad doble, por un lado nos permite **autentificar el usuario**, y por otro lado nos permite crear un ```pipeline``` para **consultar información** de la cuenta o extraer datos del usuario.



El primer paso para trabajar con esta herramienta es clonar su repositorio:

	git clone https://github.com/omab/django-social-auth


Tambien cuenta con un repositorio en [Bitbucket](https://bitbucket.org/simpler/django-social-auth#rst-header-instagram), que da algunos detalles más.



Lo más interesante es el directorio ```example```, que contiene una pequeña aplicación ```django```
que nos permite familiarizarnos un poco.

Antes de poder ejecutar el ejemplo debemos:

###  Instalar el módulo:
		
	pip install django-social-auth==0.7.25
o

	pip install django-social-auth

o 

	 easy_install django-social-auth


Una vez instalado, ya podemos realizar las configuraciones, aunque muchas de estos cambios ya viene  hechos en el mismo ejemplo voy a detallar lo más importante, puesto que debemos exportar estos cambios a nuestra propia aplicación.

##Autentificación

####En el fichero ```setting.py```
	
	INSTALLED_APPS = (
	    ...
	    'social_auth'
	)

También se incorpora ```'south'``` pero la verdad tengo idea de lo que hace.

Por ejemplo para Linkedin:

	LINKEDIN_CONSUMER_KEY = X    # The LinkedIn application "API Key"
	LINKEDIN_CONSUMER_SECRET = X # The LinkedIn application "Secret Key"

o claves que se nos proporciona cuando registramos la aplicación en la red que sea.


para Instagram hay que proporcionar:

	INSTAGRAM_CLIENT_ID = ''
	INSTAGRAM_CLIENT_SECRET = ''


para Twitter:

	TWITTER_CONSUMER_KEY = ''
	TWITTER_CONSUMER_SECRET = ''



####Creamos la base de datos:

	./manage.py syncdb
	python manage.py migrate social_auth




Después debemos añadir:

	AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.linkedin.LinkedinBackend',   #Linkedin   
	'social_auth.backends.contrib.instagram.InstagramBackend', #Instagram
    'social_auth.backends.twitter.TwitterBackend',			   #Twitter
    'social_auth.backends.facebook.FacebookBackend',		   #Facebook
	...
    'django.contrib.auth.backends.ModelBackend',
)

O el asociado a la red que nos interese.


####En el fichero ```urls.py```

	urlpatterns = patterns('',
    ...
    url(r'', include('social_auth.urls')),
    ...
)


####Seleccionar que datos:

Necesarios para autentificarse:

	LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',]

Que va a proporcionar la red social a nuesta app
	
	LINKEDIN_EXTRA_FIELD_SELECTORS = [
	    'first-name',
	    'last-name',
	    'email-address',
	    'headline', # The job title
	    'positions', # Used to retrieve the company
	]

Se supone que aquí es donde indicamos que queremos obtener las fotos o los twetts...

y que queremos que se guarden en la base de datos.

	LINKEDIN_EXTRA_DATA = [
    ('id', 'id'),
    ('first-name', 'first_name'),
    ('last-name', 'last_name'),]
     + [(field, field.replace('-', '_'), True) for field in LINKEDIN_EXTRA_FIELD_SELECTORS]


El ejemplo es con linkedin, porque no encuentro ejemplos para twitter y Instagram.

#### Por ultimo creamos una ```view``` un ejemplo puede ser:



	from django.conf import settings
	from django.http import HttpResponseRedirect
	from django.shortcuts import render_to_response
	from django.template import RequestContext 
	from django.contrib.auth.decorators import login_required
	from django.contrib.auth import logout as auth_logout
	from django.contrib.messages.api import get_messages
	# Where the user is redirected after successful authentication
	@login_required
	def complete(request): 
	    return render_to_response('auth/complete.html', {}, context_instance=RequestContext(request))
	# Since the logged in user is a normal Django user instance, we logout the user the natural Django way:
	def logout(request):
	    """Logs out user"""
	    auth_logout(request)
	    return HttpResponseRedirect('/')
	def error(request):
	    """Error view"""
	    messages = get_messages(request)
	    return render_to_response('auth/error.html', {'messages': messages}, RequestContext(request))


Añadimos las urls para que se llamen a las funciones de la vista.

	urlpatterns = patterns("",
	    ...
	    url(r"^complete/", "myapp.views.complete", name="complete"),
	    url(r"^logout/", "myapp.views.logout", name="logout"),
	    ...
	)

##Creación del pipeline

Las pipelines nos permiten recuperar información de la red social y nos permiten actualizar los datos.

Debemos añadir a setting.py

	SOCIAL_AUTH_PIPELINE =  (
    'Social_auth.backends.pipeline.social.social_auth_user' ,
    'Social_auth.backends.pipeline.user.get_username' ,
    'Social_auth.backends.pipeline.user.create_user' ,
    'Social_auth.backends.pipeline.social.associate_user' ,
    'Social_auth.backends.pipeline.social.load_extra_data' ,
    'social_auth.backends.pipeline.user.update_user_details' ,
    'Myqpp.models.social_auth_to_profile'
)


y por ejemplo en viwers.py


	def social_auth_to_profile(backend, details, response, user=None, is_new=False, *args, **kwargs):
	    if is_new:
	        profile = UserProfile.objects.get_or_create(user=user)
	    else:
	        profile = UserProfile.objects.get(user=user)
	    # Some of the default user details given in the pipeline
	    profile.email = details['email']
	    profile.name = details['fullname']
	    # Now we also need the extra details, found in the `social_user` kwarg
	    social_user = kwargs['social_user']
	    profile.company = social_user.extra_data['headline']
	    profile.job_title = social_user.extra_data['positions']['position'][0]['title']
	    profile.save()



Manual realizado con la referencia [http://gpiot.com/blog/linkedin-authentication-django-social-auth/](http://gpiot.com/blog/linkedin-authentication-django-social-auth/) y esta pensado para LinkeIn, pero pienso que puede ser una buena aproximación a Twitter y Instagram.

En fin menos da una piedra.


Tal cual posiblemente lance un error que se soluciona de la siguente forma: [https://github.com/omab/django-social-auth/commit/fc32f732d37903cd77c3de028c2d9e91b1bfbe47](https://github.com/omab/django-social-auth/commit/fc32f732d37903cd77c3de028c2d9e91b1bfbe47)

Unos vídeos interesantes pueden ser:

[Enlace a video 1](https://godjango.com/13-django-social-auth-101/)


Happy coding.

