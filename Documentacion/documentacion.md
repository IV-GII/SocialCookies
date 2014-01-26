#Práctica 4: Diseño del soporte virtual al desarrollo y despliegue de una aplicación.

## Introducción.

Esta práctica estará orientada para las asignaturas IV y DAI. Se trata de diseñar de forma ágil la máquina virtual que dará soporte para el despliegue de una aplicación web. Se pretende acercar al alumno al desarrollo de una aplicación real en un entorno de un lugar de coworking con aplicaciones sugeridas por los propios coworkers.

##Descripción de la aplicación.

Este grupo ha aceptado el proyecto propuesto por XXXXXX que consiste en desarrollar una aplicación web que permite al cliente elegir un molde de galleta y una imagen de Twitter o Instagram para imprimir en la galleta.

Para dar soporte a la aplicación hemos montado una máquina virtual en Azure con Ubuntu 13.10 que hemos configurado de forma automática con un script creado por el grupo.


##La máquina virtual.

La máquina se ha creado desde el panel web de Azure y se han establecido extremos de conexión para ftp http y django por los siguientes puertos:

	(captura de pantalla de configuración de la máquina virtual  y puertos de conexión)

Podemos ver el script de configuración [aquí](https://github.com/IV-GII/SocialCookies/blob/master/Aprovisionamiento/script.sh).

La creación de la máquina virtual por el web panel la podemos ver en la [práctica3](https://github.com/oskyar/Practica3-VirtualMachine/blob/master/documentacion/documentacion.md#1-empezaremos-creando-la-m%C3%A1quina-virtual-desde-la-p%C3%A1gina-de-azure-ya-que-es-m%C3%A1s-atractivo-e-intuitivo) de la asignatura. 


##La aplicación.




>Nota: Para alojar la aplicación en otro servidor, tendremos que cambiar la ruta de "TEMPLATE_DIR" en el fichero /SocialCookies/ENV1/webcookies/socialcookies/templates/socialcookies/settings.py

TEMPLATE_DIR = ( '<ruta_proyecto>/SocialCookies/ENV1/webcookies/socialcookies/templates/socialcookies' )


