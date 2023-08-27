from django.db import models
import datetime

# Create your models here.

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

class Corre0(models.Model):
	"""
		Correlation Table 0
		Mutable:
		One-To_One
	"""
	fbmpoint = models.OneToOneField(FBMPoint, on_delete=models.CASCADE, primary_key=True);
	mmpoint = models.OneToOneField(MMPoint, on_delete=models.CASCADE, primary_key=True);
	
	def __str__(self):
		return "%s" % (self.mmpoint);

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

class Corre1(models.Model):
	"""
		Mutable
		One-To-One
	"""
	fbmpoint = models.OneToOneField(FMBPoint, on_delete=models.CASCADE, primary_key=True);
	llpoint = models.OneToOneField(LLPoint, on_delete=models.CASCADE, primary_key=True);
	
	def __str__(self):
		return "%s" %s (self.llpoint);

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
	pke = models.CharField(max_length=50, default='0';
	
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
	pke = models.CharField(max_length=50, default='0';
	
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
	end_time = models.CharField(max_length=10, blank=True, null=True;
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
	end_time = models.CharField(max_length=10, blank=True, null=True;
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
	end_time = models.CharField(max_length=10, blank=True, null=True;
	description = models.CharField(max_length=150, blank=True, null=True);
	duration = models.FloatField(default=0);
	
	def __str__(self):
		return "%s" % (self.title);
