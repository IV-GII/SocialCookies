		
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

