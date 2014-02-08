#encoding:utf-8

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


from django.forms import ModelForm
from django import forms
from django.utils import html


class ContactForm(forms.Form):
	nombre = forms.CharField(label='Nombre completo', widget=forms.TextInput(attrs={'class':'form-control'}))
	correo = forms.EmailField(label='Correo electrónico',widget=forms.TextInput(attrs={'class':'form-control'}))
	mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
	
class PedidoForm(forms.Form):
	nombre = forms.CharField(label='Nombre completo', widget=forms.TextInput(attrs={'class':'form-control'}))
	direccion = forms.CharField(label='Direccion', widget=forms.TextInput(attrs={'class':'form-control'}))
	telefono = forms.IntegerField(label='Telefono de contacto', widget=forms.TextInput(attrs={'class':'form-control'}))	
	correo = forms.EmailField(label='Correo electrónico',widget=forms.TextInput(attrs={'class':'form-control'}))


class fotosPedido(forms.Form):

	hidden_field0 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'galletas'}))
	
    

