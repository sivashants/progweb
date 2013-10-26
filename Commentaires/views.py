# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Commentaires.forms import ConnexionForm
from django.core.urlresolvers import reverse 
from Commentaires.models import Movie, Serie
def home(request):
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
	return redirect(reverse(home))


def movies(request):
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
	movies=Movie.objects.all()
	return render(request,'Commentaires/movies.html',locals())
	#return connexion(request,'Commentaires/movies.html')

def lire(request, id):
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
	try:
		movie=Movie.objects.get(id=id)
	except movie.DoesNotExist:
	  	return HttpResponse(u"Film non trouve")
	return render(request,'Commentaires/detail.html',locals())

def serie(request):
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
	series=Serie.objects.all()
	return render(request,'Commentaires/tvShow.html',locals())
	#return connexion(request,'Commentaires/movies.html')


