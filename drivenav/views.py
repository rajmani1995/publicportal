from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from foundation.models import Mapobject,Complaint
from math import sin, acos,cos
import json
# Create your views here.


def index(request):
	return render(request,'driver/index.djt',{})

def issues(request):
	issues = Complaint.objects.filter(approved = True)
	return render(request,'driver/issues.djt',{'issues': issues})

def route(request, issue_id):
	issue = Complaint.objects.get(id = issue_id)
	return render(request,'driver/route.djt',{'issue': issue})

