from django.db import models;

# Create your models here.

class Mosebedisi(models.Model):
    username = models.CharField(max_length=50		# Maximum number of characters allowed for username.
    				,blank=True, null=True # Allows username to be left blank.
    				);
    pkn = models.BigIntegerField(default=0);		# Public key n.
    pke = models.BigIntegerField(default=0);		# Public key e.
	
    def __str__(self):
        return "%s" % (self.username);
