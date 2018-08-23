from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from . models import Contact
from . forms import Contactform


def index(request):
	#contact = Contact.objects.all()

	if request.method == 'POST':
		form = Contactform(request.POST)

		if form.is_valid():
			new_contact =Contact(firstname=request.POST['firstname'],lastname=request.POST['lastname'],
				mobileno=request.POST['mobileno'],workno=request.POST['workno'],email=request.POST['email'],
				address=request.POST['address'])
			new_contact.save()
			return redirect('index')
	else:
		form = Contactform()
		context = {'form' : form }
		return render(request,'user_example/index.html', context)


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)


		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request, user)
			return redirect('login')

	else:
		form = UserCreationForm()
	context = {'form' : form}
	return render(request,'registration/register.html', context)


def contact(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = UserCreationForm()
		context = {'form' : form }
		return render(request,'user_example/index.html', context)

		
			



	
