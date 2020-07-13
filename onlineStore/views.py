from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer

# Create your views here.

def index(request):
	return render(request, 'index.html',{})

def loginCustomers(request):
	return render(request, 'loginCustomers.html',{})

def category(request):
	return render(request, 'category.html',{})
def createAccount(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			Customer.objects.create(**form.cleaned_data)
		else :
			print(form.errors)

	context = {
		'form' :form,
	}
	return render(request, 'createAccount.html',context)