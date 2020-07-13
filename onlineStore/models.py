from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	dni = models.IntegerField()
	email = models.EmailField()
	password = models.CharField(max_length=100)
