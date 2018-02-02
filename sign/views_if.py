from sign.models import Event,Guest
from django.http import JsonResponse
from django.core.exceptions import ValidationError,ObjectDoesNotExist
import time

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

	event_limit=Event.objects.get(id=event_id).lim
	guest_limit=Guest.objects.filter(event_id=event_id)
	if len(guest_limit)>len(event_limit):
		return JsonResponse({'status':10026,'message':'event number is full'})

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


def get_guest_list(request):
	phone=request.GET.get('phone','')
	name=request.GET.get('name','')
	if phone=='' and name=='':
		return JsonResponse({'status':10021,'message':'At least input a parameter.'})

	if phone!='':
		guest={}
		try:
			result=Guest.objects.get(phone=phone)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10022,'message':'query result is empty'})
		else:
			guest['event_id']=result.event_id
			guest['realname']=result.realname
			guest['phone']=result.phone
			guest['email']=result.email
			guest['sign']=result.sign
			guest['create_time']=result.create_time
			return JsonResponse({'status':10023, 'message':'success','data':guest})
	if name!='':
		datas=[]
		try:
			results=Guest.objects.filter(realname__contains=name)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10024,'message':'Doesn not have this kind of guest'})
		else:
			for g in results:
				guest={}
				guest['event_id']=g.event_id
				guest['realname']=g.realname
				guest['phone']=g.phone
				guest['email']=g.email
				guest['sign']=g.sign
				guest['create_time']=g.create_time
				datas.append(guest)
			return JsonResponse({'status':10025,'message':'success','data':datas})


def user_sign(request):
	eid=request.GET.get('eid','')
	phone=request.GET.get('phone','')
	if eid=='' or phone=='':
		return JsonResponse({'status':10021,'message':'parameter error'})
	result=Event.objects.filter(id=eid)
	if not result:
		return JsonResponse({'status':10022,'message':'Event does NOT exist.'})

	result=Event.objects.get(id=eid).status
	if not result:
		return JsonResponse({'status':10023,'message':'Event is NOT available.'})

	event_time=Event.objects.get(id=eid).start_time
	etime=str(event_time).split('.')[0]
	timeArray=time.strptime(etime,"%Y-%m-%d %H:%M:%S")
	e_time=int(time.mktime(timeArray))

	now_time=str(time.time())
	ntime=now_time.split('.')[0]
	n_time=int(ntime)

	if n_time>=e_time:
		return JsonResponse({'status':10024,'message':'Event has started.'})

	result=Guest.objects.get(phone=phone).event_id
	if int(result)!= int(eid):
		return JsonResponse({'status':10025,'message':"The guest NOT in the event, unable to sign."})

	result=Guest.objects.get(phone=phone).sign
	if result:
		return JsonResponse({'status':10026,'message':"You have already signed in. Welcome to our party."})
	else:
		Guest.objects.filter(phone=phone).update(sign="True")
		return JsonResponse({'status':10027,'message':"Sign in successfully. Welcome!"})