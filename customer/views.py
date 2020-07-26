import json
from django.http import JsonResponse
from registration.models import user ,shopkeeper


#showing shop name as per their
#category
def shop_category(request):
	if request.method == "POST":
		print(request.body)
		data= json.loads(request.body)
		category=data['shopname']
		message=list(shopkeeper.objects.filter(category=category).values('shopname','id'))
		print(message)
	return JsonResponse(message,safe=False)	


#snd latitude and longitude 
#to find locations off shops

def location(request):
	if request.method =="POST":
		data=json.loads(request.body)
		Id=data['id']
		message=list(shopkeeper.objects.filter(id=Id).values('address'))
		print(message)
	return JsonResponse(message,safe=False)



def take_time(request):
	if request.method =="POST":
		print(request.body)
		data= json.loads(request.body)
		Id = data['id']
		timing = data['timing']
		if timeforcust.objects.filter(id=ID, timing= timing).count('people_count') <= 3 and  timeforcust.objects.filter(id=ID,timing= 
		timing).count('people_count') >=0:
			timeforcust.objects.filter(id=ID).create(**data)

		else:
			timeforcust.objects.filter(id=ID).create(**data)
		message="ok"
	return JsonResponse(message,safe=False) 	