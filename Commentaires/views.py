# Create your views here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Commentaires.forms import ConnexionForm, MovieCommentsForm, SerieCommentsForm
from django.core.urlresolvers import reverse 
from Commentaires.models import Movie, Serie, Movie_Comments, Serie_Comments
from django.contrib.auth.forms import UserCreationForm
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
	#return 

def detail_movie(request, id):
	error = False
	auth = False
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
	comments=Movie_Comments.objects.all()
	return render(request,'Commentaires/detail_movie.html',locals())


def comment_movie(request,id):
	save=False
	if request.method == 'POST':
		movie=Movie.objects.get(id=id)		
		comment=Movie_Comments(author=request.user,movie=movie)
		form = SerieCommentsForm(request.POST,instance=comment)
		if form.is_valid():
			save=True
			form.save()
		
	else:
		form = SerieCommentsForm()
	return render(request,'Commentaires/comment_movie.html',locals())	




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
	

def detail_serie(request, id):
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
		serie=Serie.objects.get(id=id)
	except serie.DoesNotExist:
	  	return HttpResponse(u"serie non trouve")
	comments=Serie_Comments.objects.all()
	return render(request,'Commentaires/detail_serie.html',locals())

def comment_serie(request,id):
	save=False
	if request.method == 'POST':
		serie=Serie.objects.get(id=id)		
		comment=Serie_Comments(author=request.user,serie=serie)
		form = SerieCommentsForm(request.POST,instance=comment)
		if form.is_valid():
			save=True
			form.save()
		
	else:
		form = SerieCommentsForm()
	return render(request,'Commentaires/comment_serie.html',locals())	




def signup(request):
	save = False
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			save=True
	else:
		form= UserCreationForm()
	return render(request,'Commentaires/signup.html',locals())	
