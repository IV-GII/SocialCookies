#!/bin/bash

#Desencriptamos las claves de instagram
cd ../ENV1/webcookies/socialcookies
sudo gpg conf.py.gpg

#Ejecutamos la aplicación
cd ..
nohup python manage.py runserver 0.0.0.0:8000