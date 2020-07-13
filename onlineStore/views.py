from django.shortcuts import render,redirect, get_object_or_404
from .forms import CustomerForm
from .models import Customer
from  django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def index(request):
	return render(request, 'index.html',{})

def loginCustomers(request):
	return render(request, 'loginCustomers.html',{})

def category(request):
	return render(request, 'category.html',{})
def createAccount(request):
	form = CustomerForm()
	context ={
		'form':form,
	}
	if request.method == 'POST':					
		dni = request.POST['dni']
		email = request.POST['email']        
		password1 = request.POST['password']
		password2 = request.POST['password2']

		if password1 == password2:
			if Customer.objects.filter(email=email).exists():
				messages.info(request,'Username Taken')
				return redirect('/createAccount')
			elif Customer.objects.filter(dni=dni).exists():
				messages.info(request,'DNI Taken')
				return redirect('/createAccount')
			else:
				form = CustomerForm(request.POST)
				if form.is_valid():										
					print(form.cleaned_data)
					Customer.objects.create(**form.cleaned_data)
					return redirect("/")				
		else:
			messages.info(request,'Password Not Matching')
			return redirect('/createAccount')						
	else:
		return render(request, 'createAccount.html',context)
	