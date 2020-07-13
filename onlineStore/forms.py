from django import forms
from .models import Customer

class CustomerForm(forms.Form):
	name = forms.CharField(label= 'Nombre',widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu Nombre'}))
	last_name = forms.CharField(label = 'Apellidos',widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu Apellido'}))
	dni = forms.IntegerField(label = 'Ingrese su DNI',widget=forms.NumberInput(attrs={'placeholder': 'Ingrese su DNI'}))
	email = forms.EmailField(label = 'Correo Electronico',widget=forms.EmailInput(attrs={'placeholder': 'example@email.com'}))
	password = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(attrs={'placeholder': 'Ingresa tu Contraseña'}))