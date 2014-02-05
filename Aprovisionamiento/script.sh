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
sudo apt-get install python-dev -y

#instalamos el gestor de modulos de python
sudo apt-get install python-pip -y


#Clonamos el repositorio de GitHub
git clone https://github.com/IV-GII/SocialCookies.git

cd SocialCookies/ENV1
source bin/activate

# Instalamos todos los paquetes especificados en requirements
sudo pip install -r requirements.txt

cd webcookies
python manage.py runserver 0.0.0.0:8000 &



