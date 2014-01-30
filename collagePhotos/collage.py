#Compose collage

#Supongamos A4     297 x 210 mm       1122x759px
#Fotos instagram   40x40 mm           150 x 150 px

##def collage(arayImg):

MARGENUP=75
MARGENOR=37
TAMPHOT =150

COL=4
FIL=5

ArrayPhotos=[]
for i in range (30):
	ArrayPhotos.append("./inst2.jpg")


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


def collage (ArayPhotos):

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
			sqX1=MARGENOR+((TAMPHOT+MARGENOR)*j)
			sqX2=MARGENOR+((TAMPHOT+MARGENOR)*j)+TAMPHOT	
			
			#print ("Foto", contPhot," : EsquinaSuperior (", sqX1," , ", sqY1," ) Esquina Inferior (" , sqX2, ", " ,sqY2," ) ")
			
			img = Image.open (ArayPhotos[contPhot])
			layerA4.paste(img, (sqX1,sqY1, sqX2, sqY2))
			contPhot=contPhot+1


	layerA4.show()
	layerA4.save("./oo.jpg")

collage(ArrayPhotos)