import json
from django.http import JsonResponse
from registration.models import user ,shopkeeper
from customer.models import shoppinglist




def list_customer(request):
	if request.method=="POST":
		print(request.body)
		data= json.loads(request.body)
		link_id=data['id']
		message=list(shoppinglist.objects.filter(link_id=link_id,Status="pending").values('key__name','date','id'))
	return JsonResponse(message,safe=False)	

#complete shopping
def finish(request):
	if request.method=="POST":
		print(request.body)
		data= json.loads(request.body)
		Id=data['id']
		shoppinglist.objects.filter(id=Id).update(Status="finish")
		message="ok"
	return JsonResponse(message,safe=False)
