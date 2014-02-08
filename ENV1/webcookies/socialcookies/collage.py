# Copyright (C) 2014  SocialCookies @IV/GII

# @anaprados @oskyar @torresj @josemlp91
# @franciscomanuel @rogegg  @pedroag  @melero90

# Aplicacion web, para gestionar pedidos de galletas,
# con fotos de Instagram y Twitter. 

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


#Compose collage

#Tamagno     A4     297 x 210 mm       1122 x 759px
#Fotos instagram   40x40 mm           150  x 150 px


INST_SIZE=150
ext = ".jpg"


MARGENUP=75
MARGENOR=37
TAMPHOT =150

COL=4
FIL=5


import os
import Image, ImageEnhance


import urllib2

def download(url, fname):
	try:
		furl = urllib2.urlopen(url)
		f = file(fname,'wb')
		f.write(furl.read())
		f.close()
	except:
		print 'Unable to download file'


def collageA4 (ArayPhotos, archivoSal ):

	contPhot=0
	sqX1=0
	sqY1=0

	sqY2=0
	sqY2=0

	layerA4 = Image.new('RGBA', (759,1122) , "white")

	for i in range (FIL):

		j=0
		sqY1=((TAMPHOT+MARGENOR)*i) + MARGENUP 
		sqY2=((TAMPHOT+MARGENOR)*i)+  TAMPHOT + MARGENUP
		
		for j in range (COL):
			if contPhot < len(ArayPhotos):
				sqX1=MARGENOR+((TAMPHOT+MARGENOR)*j)
				sqX2=MARGENOR+((TAMPHOT+MARGENOR)*j)+TAMPHOT	
				
				#print ("Foto", contPhot," : EsquinaSuperior (", sqX1," , ", sqY1," ) Esquina Inferior (" , sqX2, ", " ,sqY2," ) ")
				
				img = Image.open (ArayPhotos[contPhot])
				layerA4.paste(img, (sqX1,sqY1, sqX2, sqY2))
				contPhot=contPhot+1


	layerA4.show()
	layerA4.save(archivoSal)


def descargaAndPaste(listaURL, archivoSal):
	ArrayPhotos=[]
	for i in range (len(listaURL)):
		print (str(listaURL[i]))
		download(str(listaURL[i]), "fot"+str(i)+ext)
		img = Image.open ("fot"+str(i)+ext)
		img = img.resize((INST_SIZE, INST_SIZE), Image.NEAREST)
		img.save("fot"+str(i)+ext)

		ArrayPhotos.append("fot"+str(i)+ext)

	collageA4(ArrayPhotos,archivoSal)

	for i in range (len(listaURL)):
		os.remove("fot"+str(i)+ext)




