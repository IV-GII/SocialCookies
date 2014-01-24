#Twitter

# -*- coding: utf-8 -*-

from keys import *
import sys
import serial
import codecs
import tweepy
import re
import time

#Configuracion Arduino
PORT = 'COM3'
arduino = serial.Serial(PORT, 9600)
#


expHashtag="#\w+" #Expresion regular hashtag
expUsur="@\w+"    #Expresion regular usuario


def buscaUser(listTwit):
	listUsu=[]
	for i in range (len(listTwit)):
		if re.match(expUsur,listTwit[i]):
			listUsu.append(listTwit[i])
	return listUsu

def buscaHashtag(listTwit):
	listHash=[]
	for i in range (len(listTwit)):
		if re.match(expHashtag,listTwit[i]):
			listHash.append(listTwit[i])
	return listHash


#Autentifica y crea conexion 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


#api.update_status("#buenasnoxes @josemlp91_TIC @josemlp91_TIC creo que va a dormir bien hoy")

while True:

	result = api.user_timeline("josemlp91_TIC")

	twit=[]

	for status in result:
		twit.append(status.text.encode('utf8'))

	ultiTwit=twit[0].split(' ')

	print ultiTwit

	usuarios=(buscaUser(ultiTwit))
	hashtag=(buscaHashtag(ultiTwit))
	stringTwitt=""
	for i in range (len(usuarios)):
		stringTwitt=stringTwitt + usuarios[i]

	print (stringTwitt)

	if '#ledON' in hashtag:
		arduino.write('H')

	elif '#ledOFF' in hashtag:
		arduino.write('L')

	elif '#queVes' in hashtag:
		val=arduino.readline() # turns LED ON
		print(val)
		stringTwitt=stringTwitt+ " mis sensores dicen:  "+ str(val)
		api.update_status(stringTwitt)


 	time.sleep(10)




