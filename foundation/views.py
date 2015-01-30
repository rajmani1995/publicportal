from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from foundation.models import Mapobject,Complaint
from django.contrib.auth.models import User,AnonymousUser
import json
# Create your views here.
def render_to_json(request, data):
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
        mimetype=request.is_ajax() and "application/json" or "text/html"
    )

def sendposition(request):
	if request.method == "POST" and request.is_ajax():
		response_data={}
		latitude = request.POST.get('latitude',"")
		longitude = request.POST.get('longitude',"")
		# print "latitude"+str(latitude)+" longitude: "+str(longitude)
		user = request.user
		# print user
		mapdata = Mapobject()
		mapdata.user=user
		mapdata.latitude=latitude
		mapdata.longitude=longitude
		mapdata.save()
		response_data['message']='Successful submission'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		print "nee abba"

def complain(request):
	if request.method=="POST":
		title=request.POST.get('title',"")
		complaintype=request.POST.get('complaintype',"")
		description = request.POST.get('description',"")
		difficulty=request.POST.get('difficulty',"")
		anonycheck=request.POST.get('anonycheck',"")
		comp=Complaint()
		comp.title=title
		comp.type=complaintype
		comp.description=description
		comp.difficulty=difficulty
		if anonycheck:
			comp.user=request.user.id
		else:
			comp.user=0
		comp.save()
		return HttpResponseRedirect('/complain/')
	return render(request,'user/complaint.html',{'title':'Complain'})
	# if request.method == "POST" and request.is_ajax():
	# 	response_data={}
	# 	pass