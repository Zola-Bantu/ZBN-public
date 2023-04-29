from django.db import models

# Create your models here.

class Qrcode(models.Model):
    name = models.CharField(max_length=50	# Maximum number of characters allowed for username.
    				,blank=True, null=True      # Allows username to be left blank.
    				);
    path = models.CharField(max_length=150);	    # Public key n.
    timestamp = models.DateTimeField(auto_now_add=True);	    # Public key e.
	
    def __str__(self):
        return "%s | created at %s" % (self.name, self.timestamp);