from models import Photos
from django.shortcuts import render_to_response, get_object_or_404
import random, string, json
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


categorys={1:"landscapes",2:"people", 3:"cityscapes", 4:"stilllife",5:"animals"}
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

def get_photos_by_category(request,category_code):
	photo = Photos.objects.filter(category=categorys[int(category_code)])
	response_data=[]
	for p in photo:
		to_use={'id':p.id,'category':str(p.category),'url':str(p.httpurl)}
		response_data.append(to_use)
	return HttpResponse(json.dumps(response_data),  content_type="application/json")

def reset_category(request):
	all_photos = Photos.objects.all()
	for p in all_photos:
		p.category=''
		p.save()
	return HttpResponse(json.dumps({'res':'resetted'}),  content_type="application/json")

@csrf_exempt
def add_category(request, photo_id, category_code):
	photo = Photos.objects.get(id=photo_id)
	photo.category = categorys[int(category_code)]
	photo.save()
	return HttpResponse()


