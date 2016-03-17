#-*- coding: UTF-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

#Views for groups

def journal(request):
	return render(request, 'students/journal.html', {})

