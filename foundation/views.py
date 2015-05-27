from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from foundation.models import Mapobject,Complaint
from django.contrib import messages
from django.contrib.auth.models import User,AnonymousUser
import json
import nude

# Create your views here.
def render_to_json(request, data):
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
        mimetype=request.is_ajax() and "application/json" or "text/html"
    )

def change_file_path(comp):
	import os
	from django.conf import settings
	initial_path = comp.image.path
	comp.image.name = '/needsapproval'+ initial_path[initial_path.rindex('/'):]
	new_path = settings.MEDIA_ROOT + comp.image.name
	dir = os.path.dirname(new_path)

	try:
		os.stat(dir)
	except:
		os.mkdir(dir) 
	os.rename(initial_path, new_path)
	comp.save()

def complain(request):
	if request.method=="POST":
		title=request.POST.get('title',"")
		complaintype=request.POST.get('complaintype',"")
		description = request.POST.get('description',"")
		difficulty=request.POST.get('difficulty',"")
		lat = request.POST.get('lat',"")
		lon = request.POST.get('lon',"")
		loc = request.POST.get('loc',"")
		anonycheck=request.POST.get('anonycheck',"")
		comp=Complaint()
		# if 'picture' in request.FILES:
		comp.image = request.FILES['picture']
		print comp.image
		comp.title=title
		comp.type=complaintype
		comp.description=description
		comp.difficulty=difficulty
		comp.latitude=lat
		comp.longitude=lon
		comp.location= loc
		if not anonycheck:
			comp.userid=request.user.id
		else:
			comp.userid=0
		comp.save()
		#Using the nonude library to check and store it under needsapproval if necessary
		isnude = nude.is_nude(comp.image.path)
		if isnude == True:
			comp.approved = False;
			change_file_path(comp)
			messages.error(request,"Complaint image may have contained nudity. Approval awaiting.")
		else:
			messages.info(request,"Complaint has been registered!")
		return HttpResponseRedirect('/complain/')
	return render(request,'user/complaint.djt',{'title':'Complain'})

def viewcomplaints(request):
	complains=Complaint.objects.filter(approved = True)
	return render(request,'user/viewcomplaints.djt',{'title':'View Complaints','complains':complains})