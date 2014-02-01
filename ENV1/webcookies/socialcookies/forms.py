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

	hidden_field0 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_0'}))
	hidden_field1 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_1'}))
	hidden_field2 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_2'}))
	hidden_field3 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_3'}))
	hidden_field4 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_4'}))
	hidden_field5 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_5'}))
	hidden_field6 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_6'}))
	hidden_field7 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_7'}))
	hidden_field8 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_8'}))
	hidden_field9 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_9'}))
	hidden_field10 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_10'}))
	hidden_field11 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_11'}))
	hidden_field12 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_12'}))
	hidden_field13 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_13'}))
	hidden_field14 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_14'}))
	hidden_field15 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_15'}))
	hidden_field16 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_16'}))
	hidden_field17 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_17'}))
	hidden_field18 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_18'}))
	hidden_field19 = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id':'URL_19'}))
    

