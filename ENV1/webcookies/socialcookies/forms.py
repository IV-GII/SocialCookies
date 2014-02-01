#encoding:utf-8

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
	
    

