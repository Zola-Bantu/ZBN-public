from django.db import models

# Create your models here.

class Mosebedisi(models.Model):
	username = models.CharField(max_length = 50, blank=True, null=True)
	pkn = models.BigIntegerField(default=0)
	pke = models.BigIntegerField(default=0)
	
	def __str__(self):
		return "%s" % (self.username)
