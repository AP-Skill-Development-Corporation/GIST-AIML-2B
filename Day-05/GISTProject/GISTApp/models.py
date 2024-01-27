from django.db import models

# Create your models here.

class Student(models.Model):
	b = [
		('3','-- Select Branch --'),
		('0','Computer Science and Engineering'),
		('1','AIML'),
		('2','Others'),
	]
	rno = models.CharField(max_length=50)
	sname = models.CharField(max_length=120)
	sage = models.IntegerField(default=18)
	sbranch = models.CharField(max_length=5,choices=b,default='3')

