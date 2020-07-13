from django import forms
from .models import Customer

class CustomerForm(forms.Form):
	name = forms.CharField()
	last_name = forms.CharField()
	dni = forms.IntegerField()
	email = forms.EmailField()
	password = forms.CharField()