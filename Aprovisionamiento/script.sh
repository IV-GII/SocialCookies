#!/bin/bash


#Actualizamos la maquina
sudo apt-get update
sudo apt-get upgrade


#Instalamos el paquete de idioma (español)
sudo apt-get install language-pack-es -y

sudo apt-get install build-essential -y

#Instalamos git
sudo apt-get install git -y

#instalamos python
sudo apt-get install python -y

#instalamos el gestor de modulos de python
sudo apt-get install python-pip -y

#Configuración e instalación de django
sudo pip install django

#instalacion de modulos de python
sudo pip install tweepy
sudo pip install django-mako

#Clonamos el repositorio de GitHub
git clone https://github.com/IV-GII/SocialCookies.git

<<<<<<< HEAD
=======

>>>>>>> e9b4e7fb5236ad0c75c60f2d7753b16f86db77b9
#nos movemos a la carpeta y lo lanzamos

cd SocialCookies/ENV1
source bin/activate
cd webcookies
<<<<<<< HEAD
python manage.py runserver 0.0.0.0:8000
=======
python manage.py runserver 0.0.0.0:8000 &
>>>>>>> e9b4e7fb5236ad0c75c60f2d7753b16f86db77b9


