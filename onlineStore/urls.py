from django.urls import path
from . import views

urlpatterns = [	
	path('',views.index,name='index'),
	path('loginCustomers/',views.loginCustomers,name='loginCustomers'),
	path('category/',views.category,name='category'),
	path('createAccount/',views.createAccount,name='createAccount'),
] 