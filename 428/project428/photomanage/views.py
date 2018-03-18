from models import Photos
from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf

categorys={1:"wildlife",2:"portrait"}
# Create your views here.
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('photomanage/index.html', c)

def get_all_photos(request):
	all_photos = Photos.objects.all()
	response_data=[]
	for p in all_photos:
		to_use={'id':p.id,'category':str(p.category),'url':str(p.httpurl)}
		response_data.append(to_use)
	return HttpResponse(json.dumps(response_data),  content_type="application/json")

def add_category(request, photo_id, category_code):
	photo = Photos.objects.get(id=photo_id)
	photo.category = categorys[int(category_code)]
	photo.save()
	return HttpResponse({'res':'category assigned'})


