from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from foundation.models import Mapobject,Complaint
from django.contrib import messages
from django.contrib.auth.models import User,AnonymousUser
import json
# Create your views here.
def render_to_json(request, data):
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
        mimetype=request.is_ajax() and "application/json" or "text/html"
    )

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
		# comp.location="Warangal"
		comp.save()
		messages.info(request,"Complaint has been registered!")
		return HttpResponseRedirect('/complain/')
	return render(request,'user/complaint.djt',{'title':'Complain'})

def viewcomplaints(request):
	complains=Complaint.objects.all()
	return render(request,'user/viewcomplaints.djt',{'title':'View Complaints','complains':complains})