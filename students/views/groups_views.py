#-*- coding: UTF-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

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


