from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib import messages
from .models import Student

# Create your views here.

def greet(request):
	return HttpResponse("Welcome User!!!!!")

def greetht(self):
	return HttpResponse("<h2>Welcome</h2>")

def dg(e):
	return HttpResponse("<html><title>Example</title><body><h4>Example for html tag</h4></body></html>")

def ph(q):
	return HttpResponse("<html><title>Example</title><body><h4 style='color:green;background-color:yellow'>Example for Inline Styling</h4></body></html>")

def km(request,ty):
	return HttpResponse(f"Welcome User {ty}")

def du(request,e):
	return HttpResponse(f"Welcome User <span style='color:red'>{e}</span>")

def stdnt(request,sn,rn,yr):
	return HttpResponse(f"<h1>Student Details</h1><h4>Student Name: <span style='color:red'>{sn}</span></h4><h4>Student Roll: <span style='color:green'>{rn}</span></h4><h4>Student Year: <span style='color:yellow'>{yr}</span></h4>")


def wel(t,nm):
	return HttpResponse(f"<script>alert('Hi user {nm}!!')</script>Welcome User {nm}")

def ht(request):
	return render(request,'demo.html')

def dk(request,nme):
	return render(request,'sample.html',{'usname':nme})

def emply(request,eid,enm,eag,esr):
	z={'ed':eid,'en':enm,'eg':eag,'es':esr}
	return render(request,'emp.html',z)

def stdn(request):
	if request.method == "POST":
		a = request.POST['rn']
		b = request.POST['sn']
		c = request.POST['sy']
		d = request.POST['sb']
		return render(request,'stdetails.html',{'r':a,'n':b,'y':c,'bc':d})
	return render(request,'stdreg.html')

def home(self):
	m = Student.objects.all()
	if self.method == "POST":
		g = StudentForm(self.POST)
		if g.is_valid():
			g.save()
			messages.success(self,"User Created Successfully")
			return redirect('/')
	g = StudentForm()
	return render(self,'home.html',{'k':g,'h':m})
