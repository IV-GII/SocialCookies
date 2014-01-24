#Creamos el proyecto

django-admin.py startproject mysite

cd mysite/

python manage.py runserver

	It worked!

#Creamos la aplicación

django-admin.py startapp practica_dai

cd mysite/

nano settings.py

	INSTALLED_APPS = (
		...
		'practica_dai',
	)


cd ../practica_dai/
touch views.py

	from django.shortcuts import render
	from django.http import HttpResponse
 
	 # Create your views here.

	def hola(request):
	return HttpResponse("Hola")


cd ../mysite/
nano urls.py

	urlpatterns = patterns('',
		...

		url(r'^admin/', include(admin.site.urls)),
		url(r'^', 'practica_dai.views.hola'),
		url(r'^hola/', 'practica_dai.views.hola'),
	)


cd ..
python manage.py runserver