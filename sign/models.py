from django.db import models

# Create your models here.

class Event(models.Model):
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	lim=models.IntegerField()
	status=models.BooleanField()
	start_time=models.DateTimeField()
	create_time=models.DateTimeField()

	def __str__(self):
		return self.name

class Guest(models.Model):
	event=models.ForeignKey(Event)
	realname=models.CharField(max_length=100)
	phone=models.CharField(max_length=20)
	email=models.EmailField()
	sign=models.BooleanField()
	create_time=models.DateTimeField()

	class Meta:
		unique_together=('event','phone')

	def __str__(self):
		return self.realname

