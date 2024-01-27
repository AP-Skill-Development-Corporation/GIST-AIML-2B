from GISTApp.models import Student
from django import forms

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ["rno","sname","sage","sbranch"]
		widgets = {
		"rno": forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Roll Number",
			}),
		"sname": forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Student Name",
			}),
		"sage": forms.NumberInput(attrs={
			"class":"form-control my-2",
			"max":"99",
			"min":"18",
			}),
		"sbranch": forms.Select(attrs={
			"class":'form-control my-2',
			}),
		}
