#-*- coding: UTF-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

#Views for students
def students_list(request):
	students = (
		{'id': 1,
		 'first_name': u'Антон',
		 'last_name': u'Граменко',
		 'ticket': 6,
		 'image': 'img/Anton.jpg'},
		{'id': 2,
		 'first_name': u'Наташа',
		 'last_name': u'Холодняк',
		 'ticket': 7,
		 'image': 'img/Natalie.jpg'},
		{'id': 3,
		 'first_name': u'Дмитро',
		 'last_name': u'Граменко',
		 'ticket': 21,
		 'image': 'img/Dima.jpg'})
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

