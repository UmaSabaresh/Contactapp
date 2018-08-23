from django.db import models

class Contact(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	mobileno = models.CharField(max_length=10)
	workno =models.CharField(max_length=10)
	email = models.CharField(max_length=20)
	address = models.CharField(max_length=50)




