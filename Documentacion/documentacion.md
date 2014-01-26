#Práctica 4: Diseño del soporte virtual al desarrollo y despliegue de una aplicación.

## Introducción.

Esta práctica estará orientada para las asignaturas IV y DAI. Se trata de diseñar de forma ágil la máquina virtual que dará soporte para el despliegue de una aplicación web. Se pretende acercar al alumno al desarrollo de una aplicación real en un entorno de un lugar de coworking con aplicaciones sugeridas por los propios coworkers.

##Descripción de la aplicación.

Este grupo ha aceptado el proyecto propuesto por [Cocorocó](http://www.cocoroco.es/) que consiste en desarrollar una aplicación web que permite al cliente elegir moldes de galletas e imagenes de Twitter o Instagram para imprimir en la galleta. Mediante formularios el cliente podrá solicitar un pedido de galletas y contactar en caso de dudas.

Para dar soporte a la aplicación hemos montado una máquina virtual en Azure con Ubuntu 13.10 que hemos configurado de forma automática con un script creado por el grupo.

##La máquina virtual.

La máquina se ha creado desde el panel web de Azure y se han establecido extremos de conexión para ftp http y django por los siguientes puertos:


	(captura de pantalla de configuración de la máquina virtual y puertos de conexión)

Podemos ver como actualizamos la máquina virtual, la instalación de Python y los módulos que vamos a utilizar en el siguiente [script]
(https://github.com/IV-GII/SocialCookies/blob/master/Aprovisionamiento/script.sh). 

La creación de la máquina virtual por el web panel la podemos ver en la [práctica3](https://github.com/oskyar/Practica3-VirtualMachine/blob/master/documentacion/documentacion.md#1-empezaremos-creando-la-m%C3%A1quina-virtual-desde-la-p%C3%A1gina-de-azure-ya-que-es-m%C3%A1s-atractivo-e-intuitivo) de la asignatura.

##Uso de la aplicación

Cuando el usuario entra en la aplicación puede acceder a sus fotos iniciando sesión en [Instagram](http://instagram.com/#) o [Twitter](https://twitter.com/). Una vez dentro se le desplegará una lista con sus imágenes subidas o favoritas. El cliente seleccionará las fotos y un molde de galleta y solicitará el pedido rellenando un formulario.










