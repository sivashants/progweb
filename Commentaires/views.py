# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Commentaires.forms import ConnexionForm
from django.core.urlresolvers import reverse 
def home(request):

#	return render(request,'Commentaires/main.html')

#def connexion(request):
	error = False
	if request.method == "POST":
		form = ConnexionForm(request.POST)
     
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				login(request,user)
			else:
				error = True
	else:
		form = ConnexionForm()

	return render(request,'Commentaires/main.html',locals())

def deconnexion(request):
	logout(request)
	return redirect(reverse(connexion))


