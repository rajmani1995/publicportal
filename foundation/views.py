from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from foundation.models import Mapobject
from django.contrib.auth.models import User
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
		print "latitude"+str(latitude)+" longitude: "+str(longitude)
		user = request.user
		print user
		# mapdata = Mapobject()
		# mapdata.user=user
		# mapdata.latitude=latitude
		# mapdata.longitude=longitude
		# mapdata.save()
		response_data['message']='Successful submission'
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	else:
		print "nee abba"