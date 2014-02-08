/*

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

*/


var elegidos = new Array();
var tipo_galleta =  new Array();

function imgFunction(objeto, url){       	
	indice = elegidos.indexOf(url);
		    
	if( indice == -1 ){
		//objeto.style.border="4px solid #00bfa8";
		objeto.style.opacity=0.4;
	    elegidos.push(url);
	} 
	else{
		//objeto.style.border="none";
	    objeto.style.opacity=1;
	    elegidos.splice(indice,1);
	}
}

function galletaFunction(objeto, url){
				    
	if( tipo_galleta.length == 0){
	    	objeto.style.opacity=0.4;
	    	tipo_galleta.push(url);
	}			
	else if (tipo_galleta[0]==url) { 
	    	objeto.style.opacity=1;
	    	tipo_galleta.splice(0,1);
	}
}

function mostrarPedido(){
	var mensaje=' ';

	for (var i=0;i<elegidos.length; i++){
	     
	     mensaje = mensaje.concat(elegidos[i]);
	     mensaje = mensaje.concat("|");

	}
	mensaje=mensaje.concat(tipo_galleta[0]);

	document.getElementById("galletas").value = mensaje;    
	document.getElementById("formPed").submit();
	//alert(mensaje);
}

function Github(nombre){
	window.open("https://www.github.com/"+nombre.substring(0, nombre.length-4) );
}

