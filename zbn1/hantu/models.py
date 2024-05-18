from django.contrib.sessions.models import Session
from django.dispatch import receiver
from django.conf import settings
from django.db import models   # Generic import
from django.contrib.auth.models import AnonymousUser

from .signals import page_viewed_signal
from .utils import get_client_ip, get_info
import requests, datetime



User = settings.AUTH_USER_MODEL

# Create your models here.


# Pages viewed table
class PageViewed(models.Model):
	timestamp 	= models.DateTimeField(auto_now_add=True)
	user 		= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE) # user instance
	ip_address 	= models.CharField(max_length=50, blank=True, null=True) # IP field
	url 		= models.CharField(max_length=50)
	country 	= models.CharField(max_length=50, blank=True, null=True)
	country_code 	= models.CharField(max_length=10, blank=True, null=True)
	region 	= models.CharField(max_length=50, blank=True, null=True)
	region_code 	= models.CharField(max_length=10, blank=True, null=True)
	town 		= models.CharField(max_length=50, blank=True, null=True)
	lat 		= models.FloatField(max_length=50, blank=True, null=True)
	lon 		= models.FloatField(max_length=50, blank=True, null=True)	
	timezone 	= models.CharField(max_length=20, blank=True, null=True)
	zip_code	= models.CharField(max_length=10, blank=True, null=True)
	isp 		= models.CharField(max_length=50, blank=True, null=True)
	organization 	= models.CharField(max_length=50, blank=True, null=True)
	az 		= models.CharField(max_length=50, blank=True, null=True)
	
	def __str__(self):
		return "%s viewed on %s" % (self.url, self.timestamp)
		
	class Meta:
		ordering = ['-timestamp'] # most recent save show up first
		verbose_name = 'Page viewed'
		verbose_name_plural = 'Pages viewed'




@receiver(page_viewed_signal)
def page_viewed_reciever(sender, request, *args, **kwargs):
	"""This function recieves a signal from page_viewed_signal, runs the get_info 
	function and then puts the data into the PageViewed Table and ExtraInfo Table"""
	if request.user.__class__ == AnonymousUser:
		user = None
	else:
		user = request.user
		
	status, country, country_code, region_code, region, town, zip_code, lat, lon, timezone, isp, organization, az, query = get_info(get_client_ip(request))
	
	if status == 'success':
		page_view_obj = PageViewed.objects.create(
		user = user,
		ip_address = query,
		url = request.path,
		country = country,
		country_code = country_code,
		region = region,
		region_code = region_code,
		town = town,
		lat = lat,
		lon = lon,
		zip_code = zip_code,
		timezone = timezone,
		isp = isp,
		organization = organization,
		az = az,
		)
	
	else:
		page_view_obj = PageViewed.objects.create(
		user = user,
		ip_address = get_client_ip(request),
		url = request.path,
		)


class MMPoint(models.Model):
	"""
		Mutable:
		Moon Map Point
	"""
	name = models.CharField(max_length=50, blank=True, null=True);
	radius = models.CharField(max_length=50, blank=True, null=True);
	angle = models.CharField(max_length=3, blank=True, null=True);
	height = models.CharField(max_length=50, blank=True, null=True);
	otype = models.CharField(max_length=50, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.name);

class FBMPoint(models.Model):
	"""
		Mutable:
		Full Body Map Point
	"""
	name = models.CharField(max_length=50, blank=True, null=True);
	radius = models.CharField(max_length=50, blank=True, null=True);
	angle = models.CharField(max_length=3, blank=True, null=True);
	height = models.CharField(max_length=50, blank=True, null=True);
	otype = models.CharField(max_length=50, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.name);

class Corre0(models.Model):
	"""
		Correlation Table 0
		Mutable:
		One-To_One
	"""
	fbmpoint = models.OneToOneField(FBMPoint, on_delete=models.CASCADE);
	mmpoint = models.OneToOneField(MMPoint, on_delete=models.CASCADE);
	
	def __str__(self):
		return "%s" % (self.mmpoint);

class LLPoint(models.Model):
	"""
		Mutable:
		Leaflet Point. Interactive map.
	"""
	name = models.CharField(max_length=50, blank=True, null=True);
	longitude = models.CharField(max_length=50, blank=True, null=True);
	latitude = models.CharField(max_length=50, blank=True, null=True);
	height = models.CharField(max_length=20, blank=True, null=True);
	otype = models.CharField(max_length=50, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.name);

class Corre1(models.Model):
	"""
		Mutable
		One-To-One
	"""
	fbmpoint = models.OneToOneField(FBMPoint, on_delete=models.CASCADE);
	llpoint = models.OneToOneField(LLPoint, on_delete=models.CASCADE);
	
	def __str__(self):
		return "%s" %s (self.llpoint);



class LLPosition(models.Model):
	"""
		Immutable
		Leaflet Position.
	"""
	time_stamp = models.CharField(max_length=15, blank=True, null=True);
	longitude = models.CharField(max_length=50, blank=True, null=True);
	latitude = models.CharField(max_length=50, blank=True, null=True);
	hashKey = models.CharField(max_length=50, blank=True, null=True);
	signature = models.CharField(max_length=50, blank=True, null=True);
	pkn = models.CharField(max_length=150, default='0');
	pke = models.CharField(max_length=50, default='0');
	
	def __str__(self):
		return "%s" % (self.time_stamp);

class Header(models.Model):
	"""
		Immutable
	"""
	nounce = models.CharField(max_length=100, blank=True, null=True); # Proof of work!
	prev_hash = models.CharField(max_length=100, blank=True, null=True);
	hashKey = models.CharField(max_length=100, blank=True, null=True);
	signature = models.CharField(max_length=50, blank=True, null=True);
	pkn = models.CharField(max_length=150, default='0');
	pke = models.CharField(max_length=50, default='0');
	
	def __str__(self):
		return "%s" % (self.nounce);

class Event(models.Model):
	"""
		Mutable
	"""
	title = models.CharField(max_length=100, blank=True, null=True);
	date = models.DateField(default = datetime.date(2023,8,12));
	repeat = models.CharField(max_length=10, blank=True, null=True);
	allDay = models.BooleanField(default=False);
	start_time = models.CharField(max_length=10, blank=True, null=True);
	end_time = models.CharField(max_length=10, blank=True, null=True);
	description = models.CharField(max_length=150, blank=True, null=True);
	duration = models.FloatField(default=0);
	
	def __str__(self):
		return "%s" % (self.title);

class Reminder(models.Model):
	"""
		Mutable
	"""
	title = models.CharField(max_length=100, blank=True, null=True);
	date = models.DateField(default = datetime.date(2023,8,12));
	repeat = models.CharField(max_length=10, blank=True, null=True);
	allDay = models.BooleanField(default=False);
	start_time = models.CharField(max_length=10, blank=True, null=True);
	end_time = models.CharField(max_length=10, blank=True, null=True);
	duration = models.FloatField(default=0);
	
	def __str__(self):
		return "%s" % (self.title);

class Task(models.Model):
	"""
		Mutable
	"""
	title = models.CharField(max_length=100, blank=True, null=True);
	date = models.DateField(default = datetime.date(2023,8,12));
	repeat = models.CharField(max_length=10, blank=True, null=True);
	allDay = models.BooleanField(default=False);
	start_time = models.CharField(max_length=10, blank=True, null=True);
	end_time = models.CharField(max_length=10, blank=True, null=True);
	description = models.CharField(max_length=150, blank=True, null=True);
	duration = models.FloatField(default=0);
	
	def __str__(self):
		return "%s" % (self.title);
