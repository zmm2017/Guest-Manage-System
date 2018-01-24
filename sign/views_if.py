from sign.models import Event,Guest
from django.http import JsonResponse
from django.core.exceptions import ValidationError,ObjectDoesNotExist

def add_event(request):
	eid=request.POST.get('eid','')
	name=request.POST.get('name','')
	lim=request.POST.get('lim','')
	status=request.POST.get('status','')
	address=request.POST.get('address','')
	start_time=request.POST.get('start_time','')
	create_time=request.POST.get('create_time','')

	if eid=='' or name=='' or lim=='' or address=='' or start_time=='':
		return JsonResponse({'status':10021,'message':'parameter error'})

	result=Event.objects.filter(id=eid)
	if result:
		return JsonResponse({'status':10022,'message':'event id already exists'})

	result=Event.objects.filter(name=name)
	if result:
		return JsonResponse({'status':10023,'message':'event name already exists'})

	if status=='':
		status=1

	try:
		Event.objects.create(id=eid,name=name,lim=lim,status=int(status),address=address,start_time=start_time,create_time=create_time)
	except ValidationError as e:
		error='start_time format error.It must be in YYYY-MM-DD HH:MM:SS format'
		return JsonResponse({'status':'10024','message':'start_time format error'})

	return JsonResponse({'status':200,'message':'add event success'})

def get_event_list(request):
	eid=request.GET.get('eid','')
	name=request.GET.get('name','')

	if eid=='' and name=='':
		return JsonResponse({'status':10021,'message':'Please attach what you want to get'})

	else:
		if eid !='' and name=='':
			event={}
			try:
				result=Event.objects.get(id=eid)
			except ObjectDoesNotExist:
				return JsonResponse({'status':10022,'message':'query result id is empty'})
			else:
				event['name']=result.name
				event['lim']=result.lim
				event['address']=result.address
				event['status']=result.status
				event['start_time']=result.start_time
				event['create_time']=result.create_time				
				return JsonResponse({'status':10023,'message':'success','data':event})	

		elif name != '' and eid=='':
			datas = []
			results=Event.objects.filter(name__contains=name)
			if  results:				
				for r in results:
					event={}
					event['id']=r.id
					event['name']=r.name
					event['lim']=r.lim
					event['address']=r.address
					event['status']=r.status
					event['start_time']=r.start_time
					event['create_time']=r.create_time
					datas.append(event)
				return JsonResponse({'status':10024,'message':'success','data':datas})
			else:
				return JsonResponse({'status':10025,'message':'query result by name is empty'})

def add_guest(request):
	gid=request.POST.get('gid','')
	realname=request.POST.get('realname','')
	phone=request.POST.get('phone','')
	email=request.POST.get('email','')
	sign=request.POST.get('sign','')
	event_id=request.POST.get('event_id','')
	create_time=request.POST.get('create_time','')

	if gid=='' or realname=='' or phone=='' or email=='' or event_id=='' or create_time=='':
		return JsonResponse({'status':10021,'message':'parameter error'})

	result=Guest.objects.filter(id=gid)
	if result:
		return JsonResponse({'status':10022,'message':'Guest id already exists.'})

	result=Event.objects.get(id=event_id).status
	if not result:
		return JsonResponse({'status':10025,'message':'Event status is not available.'})

	result=Guest.objects.filter(phone=phone)
	if result:
		return JsonResponse({'status':10023, 'message':'Guest phone already exists.'})

	if sign=='':
		sign=1

	result=Event.objects.filter(id=event_id)
	if not result:
		return JsonResponse({'status':10024, 'message':'Event id is not exist.'})
	else:
		try:
			Guest.objects.create(id=gid,realname=realname,phone=phone,email=email,sign=sign,event_id=event_id,create_time=create_time)
		except ValidationError as e:
			error='start_time format error.It must be in YYYY-MM-DD HH:MM:SS format'
			return JsonResponse({'status':'10024','message':'create_time format error'})

		return JsonResponse({'status':200,'message':'add event success'})