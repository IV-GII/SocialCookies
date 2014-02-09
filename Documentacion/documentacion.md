#SocialCookies.
_______________


##Licencia

Hemos usado una licencia [GPLV2](https://github.com/IV-GII/SocialCookies/blob/master/LICENSE). Esta licencia la he generado al crear el proyecto seleccionando como tipo de licencia "LICENCE GPLV2".

_______________

Tras nuestra acogida en  Cocorocó Coworking, se nos propusieron una serie de proyectos interesante tanto por su parte formativa, como por sus visión empresarial.

Uno de ellos fue, SocialCookies, que como su nombre bien indica, tiene una gran relación con las Redes Sociales "social" y con las galletas "cookies", dos cosas que por lo general le gusta a la gente.

Poder aunar estos dos elementos, fue una de las cosas que más nos llamó la atención en un primer momento, además pensando que si conseguimos hacemos de una forma divertida y agradable para el público, se puede hacer negocio con ello.

![](http://granadadigital.es/wp-content/uploads/2014/01/12152536425_05fe6b44a4_k-500x300.jpg)

##Descripción.

En Cocorocó conocimos a un cocinero, que se dedicaba a hacer galletas personalizadas y como pudimos comprobar tenia ya unas instalaciones para producir estas curiosas galletas.

Nos comento su intentares en tener una plataforma web para su empresa y que permitiera a los clientes gestionar pedidos personalizados con fotos obtenidas de las redes sociales Instagram y Twitter.


###Requisitos.

- No se nos fijaron unos requisitos rígidos, ni en la parte del diseño ni nada concreto de la funcionalidad.

- Solo se nos pidió por parte del cocinero que los pedidos le llegaran por correo electrónico.

- Y que los pedidos se ajustasen al formato A4.

- Utilizar tecnologías aprendidas en las asignaturas de IV y DAI.

- Otro requisito era tener una versión, al finalizar el fin de semana, que estuvimos trabajando en las instalaciones de Cocorocó.


###Organización del trabajo.

Tras hacer el grupo, en la hora de clase de la asignatura de IV del primer Viernes de trabajo, se nos creo un repositorio en GitHub, dentro de la organización IV/GII a la que pertenecemos desde que comenzamos en la asignatura.

También creamos un grupo de ``Whatsapp`` para comunicarnos de forma informal.

Ademas creamos una cuenta de gmail [socialcookiesiv@gmail.es](socialcookiesiv@gmail.es), para que puedan contactar los interesados en nuestra aplicación, y ademas a esta cuenta es la que va ha recibir los pedidos de los clientes.

Nos creamos la cuenta de Twitter [@socialcommits](https://twitter.com/CookiesCommits), esta cuenta de twitter la enlazamos con GitHub usando el Hook propio, de forma que lleguen los commits con el progreso del trabajo.


También nos creamos una cuenta de Instagram, para hacer las pruebas, el usuario es SocialCookies.

Para trabajar usamos una metodología de trabajo colaborativa usando GIT y GitHub, e intentamos seguir también la metodología scrum, intentando siempre tener algo que funcionase.

Esta metodología consiste en crear ``Milestones`` para cada sección del trabajo que estamos realizando, y para cada sección creamos ``Issues`` que se asignaban a los distintos componentes del grupo. 
Cuando se concluía un trabajo se cerraba el Issue y se pasaba a completar otro Issue.

Esta forma de trabajar la intentamos hacer rígida, pero muchas veces al no tener experiencia nos debíamos cuenta que un determinado ``Issue`` requería más trabajo del pensado y debíamos ocuparnos más compañeros de los iniciales.

También aprovechamos la facilidad que nos da Git para integrar y combinar los cambios.


##Tecnología utilizada.

La aplicación la hemos desarrollado haciendo uso del framework Django que respeta la filosofia  "Model-Template-View". Además hemos usado como plantilla un "Bootstrap" que nos hemos descargado de [aquí](http://getbootstrap.com/).

Hemos subido nuestra aplicación a una máquina virtual de Azure la cual podemos ver [aquí](http://socialcookies.cloudapp.net/socialcookies/)

Para encriptar las claves de Instagram hemos usado la herramienta GPG que es libre.

También hemos usado la tecnología SMTP para el énvio de mensajes desde la aplicación web al correo del cocinero.


##Aprovisionamiento.

### Descripción

Para poder acceder a traves de internet a nuestra aplicación, decidimos desplegarla en una maquina virtual creada en azure. Además,
dado que somos muchos, para funcionar mejor se decidió que solo un miembro del grupo se encargaría de hacer las pruebas en el 
servidor, según fuera avanzando la aplicación. Por otro lado, nos pareció una buena idea separar, por un lado el despliegue y por otro lado los test. Es por ello que se han creado dos maquinas virtuales, una solo para los test y otro para el despliegue.

![captura de las maquinas en azure](https://dl.dropboxusercontent.com/u/17453375/azure-socialcookies.png)

La configuración de ambas es identica, se crearon siguiendo las plantillas de azure con ubuntu server 13.10 y se le añadieron
los extremos para http, ssh y sftp. Hay que destacar que el extremo http esta modificado para que rediriga las conexiones públicas 
en el puerto 80, al puerto privado 8000 que es donde esta el servidor django. 

Con ambas maquinas creadas, el siguiente paso es aprovisionarlas. Por comodidad, y para evitar instalar cosas innecesarias en
los servidores, hemos optado por usar ansible. Esto nos permite aprovisionar las dos maquinas a la vez o solo una segun queramos.
Nosotros hemos optado por separar los aprovisionamintos. El motivo es que, aunque son iguales, puede que una maquina este apagada
y la otra no y para evitar errores hay dos archivos de recetas.

Ansible se basa en dos archivos:

* ansible_hosts: Donde se agrupan las maquinas a configurar bajo un alias

* archivo.yml: Es el archivo que indica que maquinas y acciones se llevarán a cabo

Ansible no solo permite instalar todos los paquetes necesarios para lanzar el servidor, también nos permite lanzar el propio servidor
de forma remota. Aunque es lo mas lógico, y los mas simple, nosotros separamos el aprovisionamiento del despliegue. Nuestra aplicación
tiene, por motivos de seguridad, un archivo encriptado. Este archivo es el "conf.py" en el que están las claves de instagram. Para que
la aplicación funcione, es necesario desencriptarlo con gpg usando una clave. Este proceso no ha podido hacerse con ansible, ya que 
es interactivo, es decir, la terminal se queda esperando a que introduzcamos la clave, por lo que era necesario sacarlo de la receta
de ansible. Para desencriptar y lanzar el servidor hay un script "despliegue.sh".

### Archivo con los hosts de ansible

Este archivo, como ya se ha comentado, es el que contiene el alias y las direccións de las maquinas. Como nostros tenemos un servidor 
de test y otro de despliegue, se han creado dos grupos.

	[servidor]
	socialcookies.cloudapp.net

	[test]
	test-cookies.cloudapp.net


### Archivo de recetas de ansible

En este archivo debemos indicar todo lo que se va a instalar o ejecutar en la máquina indicada. Como hemos descrito anteriormente,
tenemos uno para la máquina de test y otro para la de despliegue.

test-socialcookies.yml:

	---
	- hosts: test
	  sudo: yes
	  tasks:
	    - name: Instalar build-essential
	      apt: name=build-essential state=present
	    - name: Instalar python
	      apt: name=python state=present
	    - name: Instalar python-dev
	      apt: name=python-dev state=present
	    - name: Instalar python-pip
	      apt: name=python-dev state=present
	    - name: Instalar python-imaging
	      apt: name=python-imaging state=present
	    - name: Crear enlace libfreetype.so
	      command: ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
	      ignore_errors: True
	    - name: Crear enlace libjpeg.so
	      command: ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
	      ignore_errors: True
	    - name: Crear enlace libz.so
	      command: ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
	      ignore_errors: True
	    - name: Instalar módulos de Python necesarios
	      command: pip install django django-mako tweepy python-instagram Image PIL
	    - name: Instalar git
	      apt: name=git state=present
	    - name: Descargamos la aplicación de github
	      action: git repo=https://github.com/IV-GII/SocialCookies.git dest=./SocialCookies
	      tags: deploy


socialcookies.yml:

	---
	- hosts: servidor
	  sudo: yes
	  tasks:
	    - name: Instalar build-essential
	      apt: name=build-essential state=present
	    - name: Instalar python
	      apt: name=python state=present
	    - name: Instalar python-dev
	      apt: name=python-dev state=present
	    - name: Instalar python-pip
	      apt: name=python-dev state=present
	    - name: Instalar python-imaging
	      apt: name=python-imaging state=present
	    - name: Crear enlace libfreetype.so
	      command: ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
	      ignore_errors: True
	    - name: Crear enlace libjpeg.so
	      command: ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
	      ignore_errors: True
	    - name: Crear enlace libz.so
	      command: ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
	      ignore_errors: True
	    - name: Instalar módulos de Python necesarios
	      command: pip install django django-mako tweepy python-instagram Image PIL
	    - name: Instalar git
	      apt: name=git state=present
	    - name: Descargamos la aplicación de github
	      action: git repo=https://github.com/IV-GII/SocialCookies.git dest=./SocialCookies
	      tags: deploy


En ambos puede verse que se instalan los mismos paquetes y que por ultimo se clona el repositorio del proyecto. La unica diferencia
esta en la segunda línea, en la que indicamos los hosts. También hay que comentar que para que el módulo de pithon "PIL" funcione
correctamente con la generación de imagenes, previamente a su isntalación, debemos crear tres enlaces. Si esto no se hace bien,
cuando intentamos procesar el pedido la página dará un error al crear la imagen que se enviará al repostero. También podemos observar
que hemos usado la directiva "ignore_errors" para que si los enlaces ya existierna, no se pare ansible y siga con el resto del 
playbook.


### Script de despliegue

Por último, tenemos el script que se encargará de desencriptar el archivo conf.py y de lanzar el servidor en la maquina.

	#!/bin/bash

	#Desencriptamos las claves de instagram
	cd ../ENV1/webcookies/socialcookies
	sudo gpg conf.py.gpg

	#Ejecutamos la aplicación
	cd ..
	nohup python manage.py runserver 0.0.0.0:8000 &


Vemos que es un script muy sencillo que solo se mueve por las carpetas, desencripta el archivo con gpg, y despues lanza el servidor 
django. El comando nohup hace que no se mate este proceso cuando se cierre la conexión ssh. Además es necesario añadir al final el
0.0.0.0:8000 para que escuche peticiones desde el exterior de la maquina virtual.


### Proceso de aprovisionamiento y despliegue

Una vez comentados toas las tecnologías usadas y los archivos necesarios, vamos a explicar como llevarlo a la práctica. Dado que es 
igual para la maquina de test y de despligue, nos vamos a centrar en una de ellas.

Necesitamos descargar a nuestro ordenador local los archivos de ansible para, desde él, aprovisionar la maquina virtual de forma 
remota. Solo necesitamos los archivos de ansible indicados anteriormente (ansible_hosts y los archivos *.yml). Estos se encuentran
en el [proyecto](https://github.com/IV-GII/SocialCookies/tree/master/Aprovisionamiento).

Primero aprovisionamos con ansible. Hay que entender el concepto que subyace cuando usamos este sistema. Realmente lo único que ocurre
es que se abre una conexión ssh con el host (o los hosts) y se ejecutan los comandos, pero ansible debe estar instalado en la
maquina de la persona que quiere provisionar, no en el servidor.Por ello, lo primero y mas evidente es tener acceso mediante ssh.
Como en el desarrollo de nuestra aplicación solo una persona se encargaba de hacer los test y de subirla a la maquina de despliegue,
se configuró la autentificación mediante llave publica/privada RSA para que solo esa persona accediera. El siguiente paso es indicar 
a ansible donde esta el archivo con los hosts exportando la variable.

	export ANSIBLE_HOSTS="ruta del archivo"


Con esto ya podemos proceder a lanzar ansible indicandole que archivo de recetas se va a usar, e implicitamente en que maquina/as.

	ansible-playbook socialcookies.yml


![captura de las maquinas en azure](https://dl.dropboxusercontent.com/u/17453375/azure-socialcookies2.png)


Ahora que ya tenemos la maquina con todos los paquetes necesarios, tenemos que conectarnos mediante ssh. Dentro podemos ver
que se ha clonado el poyecto y podemos movernos a la carpeta "SocialCookies/Aprovisionamiento". En ella estan los archivos de
ansible descargados antes, y el script "despliegue.sh". Después de ejecutarlo, nos pedirá una clave para desencriptar el archivo
con las llaves de instagram, y poder así lanzar el servidor.


![captura de las maquinas en azure](https://dl.dropboxusercontent.com/u/17453375/azure-socialcookies3.png)

![captura de las maquinas en azure](https://dl.dropboxusercontent.com/u/17453375/azure-socialcookies4.png)

![captura de las maquinas en azure](https://dl.dropboxusercontent.com/u/17453375/azure-socialcookies5.png)

Podemos ver que la [aplicación](http://socialcookiesiv.cloudapp.net/socialcookies/) funciona perfectamente, aunque cerremos la terminal con la conexión ssh.



##Diseño web.

Podemos acceder a la aplicación web desde este enlace [socialcookies](http://socialcookiesiv.cloudapp.net/socialcookies/) que está subida a una máquina virtual de azure. 

En el index hemos puesto un slider que contendrá diferentes fotos de galletas. Ha sido creado de forma dinámica en el "index.html", de forma que cuando se introduzcan nuevas fotos o se eliminen en el slider aparezcan correctamente sin tener que modificar el codigo.

Justo debajo hemos puesto una foto con los integrantes del equipo y cada foto contiene enlaces a sus perfiles de githup. Además justo debajo de los integrantes hemos puesto a los profesores que han organizado este evento (JJ, Sergio, Jose María).

La pestaña "Conectar de Instagram" permite al cliente acceder a sus fotos de Instagran mediante su nombre de usuario y contraseña. Una vez que haya iniciado sesión le aparecerán sus fotos personales y las fotos más populares de la red. Justo debajo aparecen los diferentes modelos de galletas de forma que el cliente lo que haría seria seleccionar las fotos que deseea y un solo modelo de galleta (si quiere escoger varios modelos de galleta tendrá que realizar tantos pedidos como modelos desee) y seleccionaría sobre el boton de énviar produciendose el procesamiento de las imagenes. Además aparecerá un formulario para que el cliente rellene con sus datos personales. Al concluir esta operación se enviará un correo al cocinero con las imagenes y los datos personales del cliente.

La pestaña "Conecta con twitter" esta en reformas.

La última pestaña "Contacto" contiene un formulario con el cual el cliente puede contactar con el cocinero para cualquier duda de cualquier tipo.

Todas las imagenes usadas en la aplicación web, y que no son nuestras, tienen indicada la dirección de la que se ha descargado, 
para no violar derechos de propiedad de las mismas.


##Conexión con redes sociales.


Una de la pieza central de nuestra aplicación es hacer que se conecte con las redes sociales antes citadas ("gmail", "twitter", "instagram") y que sea tanto de obtener como enviar información.

####Instagram

- Para Instagram usamos una api espcifica  para python ``python-instagram``.

A grandes rasgos la configuración que hemos realizado es la siguiente:

1. Registrar cliente de Instagram.

![](https://github.com/IV-GII/SocialCookies/blob/master/capturas/Instagram_cliente.png?raw=true)

2. Incorporar ``CLIENT_ID`` y ``CLIENT SECRET`` a nuestro script python, (debemos tener en cuenta que esto es secreto y no podemos incorporarlo en texto claro a github, por ello lo ciframos usando la herramienta gpg).

3. Lo primero que debemos hacer al intentar conectar con instagram, es redireccionar a una url que se genera automáticamente y que nos lleva a una pantalla de logueo.

		url=unauthenticated_api.get_authorize_url(scope=["likes","comments"]) 
	
Una vez se realice el logueo, optenemos el ``access_token`` que nos permite crear una instancia de la conexión.

	api = client.InstagramAPI(access_token=access_token)


Ya podemos obtener las fotos recientes del usuario logueado usando:

	api.user_recent_media(count)

o las fotos populares:

	api.media_popular(count)


**Siendo (count) el numero de fotos que queremos obtener**

Ya podemos almacenar las url de las imágenes en arrays para poder manejaras posteriormente. 

####Twitter

La parte de twitter tuvimos problemas con la autentifican, y no pudimos dedicarle más tiempo, así que nos pareció mas interesante trabajar con Instagram ya que es una cosa más novedosa.

Sí que hicimos un progresos en twitter utilizando el micro framework web.py pero al importar los cambios a Django, no conseguimos hacerlo funcionar.

####Gmail

 Tuvimos que añadir unas líneas en el archivo "setting.py" indicando el servidor smtp, el nombre del correo donde se envía cada mensaje, la contraseña y el puerto.

~~~

	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_HOST_USER = 'socialcookiesiv@gmail.com'
	EMAIL_HOST_PASSWORD = 'IVsocialcookies'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True

~~~

y mandar correos con archivos adjuntos.


~~~

	email = EmailMessage(titulo, contenido, to=['socialcookiesiv@gmail.com']) 
	email.attach_file('archivoSal.jpg')
	email.send()

~~~~


##Problemas planteados.

Uno de los problemas que más nos entretuvo fué conseguir enviar un correo desde nuestra aplicación. Al principio nos comentó Jose María que gmail daba muchos problemas y que nos resultaría casi imposible conseguir enviar un correo con gmail así que lo intentamos con hotmail. Intentamos configurarlo durante una hora pero no hubo forma, así que se nos ocurrió intentarlo con gmail y en 5 minutos ya estabamos enviando correos desde nuestra aplicación. Simplemente tuvimos que añadir unas líneas en el archivo "setting.py" indicando el servidor smtp, el nombre del correo donde se envía cada mensaje, la contraseña y el puerto.

##Posibles mejoras.

- Finalizar la sección de Twitter.
- Superponer molde e imagen seleccionada para ver el aspecto final de la galleta personalizada.
- Poder realizar un pedido con varios modelos de galletas.
- Poder realizar un pedido con varias unidades de una galleta con un molde e imagen.


##Reflexiones y valoración del trabajo.

Esta práctica ha sido muy diferente a las demás realizadas este curso. Podemos enfocar el aprendizaje desde el punto de vista
de las materias de las asignaturas aplicadas al desarrollo de una aplicación, pero la realidad es que la situación nos ha obligado
a ir mas allá de lo aprendido en las aulas. El hecho de tener que desarrollar una página web sobre un tema ofertado ha hecho que 
tengamos una idea mas cercana de lo que supone una relación entre un cliente y un conjunto de desarrolladores. Y además, precisamente
por tener que satisfacer las demandas del cliente, ha conllevado que tengamos que investigar e incorporar cosas que no habiamos
visto antes o en las que no nos sentíamos tan comodos. Ser capaces de llevarlo a cabo es, además de una satisfacción personal, 
un ejemplo de que somos capaces de poner en práctica lo aprendido y adaptarnos según la situación lo requiera.

Tambíen podemos enfocar la practica desde el punto de vista del trabajo en grupo. Nosotros somos 8 y aunque parezca que una ventaja, 
la realidad es que puede ser un arma de doble filo. Desde el primer momento supimos que la clave para realizar con exito la 
aplicación, y tener algo funcional para la exposición, era la organización. Perder una hora el primer día en organizarnos, supuso
un avance grandísimo en el trascurso del finde semana. Además pudimos sacar aun mas partido a github, y comprobamos la potencia
que tiene para ayudarnos a coordinar y supervisar el avance del software en desarrollo. El sistema de trabajo hizo que aunque 
delimitaramos las tareas, la filosofía coworking era evidente ya que nos fuimos ayudando y solventando dudas unos a otros mejorando
la experiencia del trabajo en equipo. En este sentido estamos muy satisfechos con nuestro trabajo, al margen del resultado.

También hay que destacar la experiencia en cocoroco, donde no hay barreras arquitectónicas y donde pudimos constatar de primera
mano poder estar rodeado de gente, que pese a no estar haciendo nada que tenga que ver con lo tuyo, te permitía acercarte y preguntar
o intentar ayudar a cuaquiera.

En definitiva, creemos que ha sido una experiencia muy positiva que nos ha permitido tener un primer contacto con la realidad que
nos vamos a encontrar fuera de la seguridad que te ofrece un aula y dónde la diferencia entre hacer bien o mal algo solo repercute en
una peor nota mientras que fuera te juegas tu prestigio o tu sueldo.

Todos estamos de acuerdo en que hemos aprendido mas allá de las materias de las asignaturas y que está experiencia nos hace
estar mejor preparados.

##Fuentes.

######_Imágenes del carrusel:_
- [http://www.eladerezo.com/wp-content/uploads/2006/10/Galletas-de-Chocolate-520x347.jpg](http://www.eladerezo.com/wp-content/uploads/2006/10/Galletas-de-Chocolate-520x347.jpg)

- [http://recetasdecocinablog.com/wp-content/uploads/2013/03/galletas-de-jengibre.jpg](http://recetasdecocinablog.com/wp-content/uploads/2013/03/galletas-de-jengibre.jpg)

- [http://runrun.es/wp-content/uploads/2012/06/galletas-de-jengibre-647x442.jpg](http://runrun.es/wp-content/uploads/2012/06/galletas-de-jengibre-647x442.jpg)


######_Framework css:_

- [http://getbootstrap.com/](http://getbootstrap.com/)

######_API's:_

- [http://instagram.com/developer/#](http://instagram.com/developer/#)


## Desarrolladores

* Ana belen Rodriguez Prados ([anaprados](https://github.com/anaprados))

* Óscar R. Zafra Megías ([oskyar](https://github.com/oskyar))

* José Miguel López Pérez ([josemlp91](https://github.com/josemlp91))

* Rogelio Gil García ([rogegg](https://github.com/rogegg))

* Pedro Alcalá Galiano ([pedroag](https://github.com/pedroag))

* Antonio Melero Bello ([melero90](https://github.com/melero90))

* Francisco Manuel Sánchez Ramos ([franciscomanuel](https://github.com/franciscomanuel))

* Jaime Torres Benavente ([torresj](https://github.com/torresj))

