from django.shortcuts import render
from foundation.models import Mapobject
from django.contrib.auth.models import User
# Create your views here.
def render_to_json(request, data):
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
        mimetype=request.is_ajax() and "application/json" or "text/html"
    )

def getData(request):
	if request.method=="POST":
		latitude = request.POST['latitude']
		longitude = request.POST['longitude']
		user = request.user
		mapdata = Mapobject()
		mapdata.user=user
		mapdata.latitude=latitude
		mapdata.longitude=longitude
		mapdata.save()
		data = {
			'msg':"Success",
		}
		return render_to_json(request,data)