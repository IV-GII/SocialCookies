#SocialCookies.
_______________

Tras nuestra acogida en  Cocorocó Coworking, se nos propusieron una serie de proyectos interesante tanto por su parte formativa, como por sus visión empresarial.

Uno de ellos fue, SocialCookies, que como su nombre bien indica, tiene una gran relación con las Redes Sociales "social" y con las galletas "cookies", dos cosas que por lo general le gusta a la gente.

Poder aunar estos dos elementos, fue una de las cosas que más nos llamó la atención en un primer momento, además pensando que si conseguimos hacemos de una forma divertida y agradable para el público, se puede hacer negocio con ello.


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

Ademas creamos una cuenta de gmail socialcookiesiv@gmail.es, para que puedan contactar los interesados en nuestra aplicación, y ademas a esta cuenta es la que va ha recibir los pedidos de los clientes.

Nos creamos la cuenta de Twitter @socialcommits, esta cuenta de twitter la enlazamos con GitHub usando el Hook propio, de forma que lleguen los commits con el progreso del trabajo.


También nos creamos una cuenta de Instagram, para hacer las pruebas, el usuario es SocialCookies.

Para trabajar usamos una metodología de trabajo colaborativa usando GIT y GitHub, e intentamos seguir también la metodología scrum, intentando siempre tener algo que funcionase.

Esta metodología consiste en crear ``Milestones`` para cada sección del trabajo que estamos realizando, y para cada sección creamos ``Issues`` que se asignaban a los distintos componentes del grupo. 
Cuando se concluía un trabajo se cerraba el Issue y se pasaba a completar otro Issue.

Esta forma de trabajar la intentamos hacer rígida, pero muchas veces al no tener experiencia nos debíamos cuenta que un determinado ``Issue`` requería más trabajo del pensado y debíamos ocuparnos más compañeros de los iniciales.

También aprovechamos la facilidad que nos da Git para integrar y combinar los cambios.


##Tecnología utilizada.

La aplicación la hemos desarrollado haciendo uso del framework Django que respeta la filosofia  "Model-Template-View". Además hemos usado como plantilla un "Bootstrap" que nos hemos descargado de [aquí](http://getbootstrap.com/).

Hemos subido nuestra aplicación a una máquina virtual de Azure la cual podemos ver [aquí](http://socialcookiesiv.cloudapp.net/socialcookies/)

Para encriptar las claves de Instagram hemos usado la herramienta GPG que es libre.

También hemos usado la tecnología SMTP para el énvio de mensajes desde la aplicación web al correo del cocinero.


##Aprovisionamiento.


##Diseño web.

Podemos acceder a la aplicación web desde este enlace [socialcookies](http://socialcookiesiv.cloudapp.net/socialcookies/) que está subida a una máquina virtual de azure. 

En el index hemos puesto un slider que contendrá diferentes fotos de galletas. Ha sido creado de forma dinámica en el "index.html", de forma que cuando se introduzcan nuevas fotos o se eliminen en el slider aparezcan correctamente sin tener que modificar el codigo.

Justo debajo hemos puesto una foto con los integrantes del equipo y cada foto contiene enlaces a sus perfiles de gitup. Además justo debajo de los integrantes hemos puesto a los profesores que han organizado este evento (JJ, Sergio, Jose María).

La pestaña "Conectar de Instagram" permite al cliente acceder a sus fotos de Instagran mediante su nombre de usuario y contraseña. Una vez que haya iniciado sesión le aparecerán sus fotos personales y las fotos más populares de la red. Justo debajo aparecen los diferentes modelos de galletas de forma que el cliente lo que haría seria seleccionar las fotos que deseea y un solo modelo de galleta (si quiere escoger varios modelos de galleta tendrá que realizar tantos pedidos como modelos desee) y seleccionaría sobre el boton de énviar produciendose el procesamiento de las imagenes. Además aparecerá un formulario para que el cliente rellene con sus datos personales. Al concluir esta operación se enviará un correo al cocinero con las imagenes y los datos personales del cliente.

La pestaña "Conecta con twitter" esta en reformas.

La última pestaña "Contacto" contiene un formulario con el cual el cliente puede contactar con el cocinero para cualquier duda de cualquier tipo.


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



##Problemas planteados.

Uno de los problemas que más nos entretuvo fué conseguir enviar un correo desde nuestra aplicación. Al principio nos comentó Jose María que gmail daba muchos problemas y que nos resultaría casi imposible conseguir enviar un correo con gmail así que lo intentamos con hotmail. Intentamos configurarlo durante una hora pero no hubo forma, así que se nos ocurrió intentarlo con gmail y en 5 minutos ya estabamos enviando correos desde nuestra aplicación. Simplemente tuvimos que añadir unas líneas en el archivo "setting.py" indicando el servidor smtp, el nombre del correo donde se envía cada mensaje, la contraseña y el puerto.

##Posibles mejoras.

- Finalizar la sección de Twitter.
- Superponer molde e imagen seleccionada para ver el aspecto final de la galleta personalizada.
- Poder realizar un pedido con varios modelos de galletas.
- Poder realizar un pedido con varias unidades de una galleta con un molde e imagen.


##Reflexiones y valoración del trabajo.

##Fuentes.

######_Imágenes del carrusel:_
- [http://www.eladerezo.com/wp-content/uploads/2006/10/Galletas-de-Chocolate-520x347.jpg](http://www.eladerezo.com/wp-content/uploads/2006/10/Galletas-de-Chocolate-520x347.jpg)

- [http://recetasdecocinablog.com/wp-content/uploads/2013/03/galletas-de-jengibre.jpg](http://recetasdecocinablog.com/wp-content/uploads/2013/03/galletas-de-jengibre.jpg)

- [http://runrun.es/wp-content/uploads/2012/06/galletas-de-jengibre-647x442.jpg](http://runrun.es/wp-content/uploads/2012/06/galletas-de-jengibre-647x442.jpg)


######_Framework css:_

- [http://getbootstrap.com/](http://getbootstrap.com/)

######_API's:_

- [http://instagram.com/developer/#](http://instagram.com/developer/#)






>>>>>>> 71b8312867b2269601daa9cbdf4646f3856afc62
