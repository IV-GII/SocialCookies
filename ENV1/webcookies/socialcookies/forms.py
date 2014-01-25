#encoding:utf-8

from django.forms import ModelForm
from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(label='Nombre completo', widget=forms.TextInput(attrs={'class':'form-control'}))
	correo_electronico = forms.EmailField(label='Correo electrónico',widget=forms.TextInput(attrs={'class':'form-control'}))
	mensaje = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))