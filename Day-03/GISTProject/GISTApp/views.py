from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request):
	return HttpResponse("Welcome User!!!!!")

def greetht(self):
	return HttpResponse("<h2>Welcome</h2>")