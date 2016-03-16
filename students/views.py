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

#Views for groups

def groups_list(request):
	groups = (
		{'id': 1,
		 'group_name': u'ЕС-31',
		 'leader': u'Граменко'},
		{'id': 2,
		 'group_name': u'Калинка',
		 'leader': u'Граменко'},
		{'id': 3,
		 'group_name': u'Боді-скалпт',
		 'leader': u'Холодняк'},)
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)


