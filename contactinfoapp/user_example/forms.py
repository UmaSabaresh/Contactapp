from django import forms

class Contactform (forms.Form):
	firstname = forms.CharField(max_length=20)
	lastname = forms.CharField(max_length=20)
	mobileno = forms.CharField(max_length=10)
	workno =forms.CharField(max_length=10)
	email = forms.CharField(max_length=20)
	address = forms.CharField(max_length=50)
	