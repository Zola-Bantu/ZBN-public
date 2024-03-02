from django.db import models

# Create your models here.
class Account(models.Model):
	"""
		Account is a One-to-one relation with Transaction.
	"""
	pkn = models.CharField(max_length=150, default='0');	    # Public key n.
	pke = models.CharField(max_length=50, default='0');	    # Public key e.
	verified = models.BooleanField(default=False);
	
	def __str__(self):
		return "%s" % (self.verified);

class Security(models.Model):
	"""
		Here we will keep vital security information any activity outside these zones 
		will trigger an alert, verification and be followed in on.
	"""
	account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True);
	known_country = models.CharField(max_length=100, blank=True, null=True);
	known_region = models.CharField(max_length=100, blank=True, null=True);
	known_city = models.CharField(max_length=100, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.verified);
	

class Payment(models.Model):
	"""
		Immutable.
		Actually many-to-many, may need to come back for relook at
		'sender' and 'receiver'		
	"""
	sender = models.ManyToManyField(Account);
	receiver = models.ManyToManyField(Account, related_name="receiver");
	amount = models.CharField(max_length=100, blank=True, null=True);
	upo = models.CharField(max_length=100, blank=True, null=True); #Unspent payment output
	hashKey = models.CharField(max_length=150, blank=True, null=True);
	signature = models.CharField(max_length=100, blank=True, null=True);
	
	def __str__(self):
		return "%s" % (self.upo);

class Header(models.Model):
	"""
		Immutable
	"""
	nounce = models.CharField(max_length=100, blank=True, null=True);
	prev_hash = models.CharField(max_length=100, blank=True, null=True);
	hashKey = models.CharField(max_length=100, blank=True, null=True);
	signature = models.CharField(max_length=100, blank=True, null=True);
	pkn = models.CharField(max_length=5000, default='0');	    # Public key n.
	pke = models.CharField(max_length=100, default='0');	    # Public key e.
	
	def __str__(self):
		return "%s" % (self.nounce);
