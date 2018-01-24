from django.contrib import admin
from sign.models import Event
from sign.models import Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
	list_display=['name','address','lim','status','start_time','create_time']
	search_fields=['name','address','lim','status','start_time','create_time']
	list_filter=['status']

class GuestAdmin(admin.ModelAdmin):
	list_display=['event','realname','phone','email','sign','create_time']
	list_filter=['sign']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
