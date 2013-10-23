# Create your views here.
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
def home (request):
	return HttpResponse ("welcome!!!")

def tpl (request):
	return render(request,'blog/tpl.html',{'current_date':datetime.now()})

