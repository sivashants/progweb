# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
def home(request):

	return render(request,'Commentaires/log.html')

def logedin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return render(request,'Commentaires/tpl.html')
		else:
			return HttpResponse(u"echec connexion")

	else:
		return HttpResponse(password)
